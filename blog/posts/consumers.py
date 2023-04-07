from django.db.models import F
from django.shortcuts import get_object_or_404
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.decorators import database_sync_to_async
from djangochannelsrestframework.mixins import (
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    DeleteModelMixin,
)

from .models import Post, Comment, User
from .consumer_serializers import PostSerializer, CommentSerializer, PostListSerializer, CommentRetrieveSerializer
from .consumer_permissions import PostPermissions, CommentPermissions, is_user_logged_in


@database_sync_to_async
def update_user_incr(user):
    if is_user_logged_in(user):
        User.objects.filter(pk=user.pk).update(status=F('status') + 1)


@database_sync_to_async
def update_user_decr(user):
    if is_user_logged_in(user):
        User.objects.filter(pk=user.pk).update(status=F('status') - 1)


class ActivityStatusConsumer:

    async def connect(self):
        await self.accept()
        await update_user_incr(self.scope['user'])

    async def disconnect(self, code):
        await update_user_decr(self.scope['user'])


class PostConsumer(ActivityStatusConsumer, GenericAsyncAPIConsumer, ListModelMixin, DeleteModelMixin, CreateModelMixin):
    queryset = Post.objects.all()
    permission_classes = (PostPermissions, )

    def get_serializer_class(self, **kwargs):
        if kwargs.get('action') == 'list':
            return PostListSerializer
        return PostSerializer

    def get_queryset(self, **kwargs):
        if kwargs.get('action') == 'list':
            user = get_object_or_404(User, username=kwargs.get('username'))
            posts = Post.objects.filter(author=user)
            return posts
        return Post.objects.all()

    def perform_create(self, serializer, **kwargs):
        return Post.objects.create(title=serializer.data.get('title'), content=serializer.data.get('content'),
                                   author=self.scope['user'])


class CommentConsumer(ActivityStatusConsumer, GenericAsyncAPIConsumer, RetrieveModelMixin, DeleteModelMixin,
                      CreateModelMixin):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (CommentPermissions, )

    def get_serializer_class(self, **kwargs):
        if kwargs.get('action') == 'retrieve':
            return CommentRetrieveSerializer
        return CommentSerializer

    def perform_create(self, serializer, **kwargs):
        post = get_object_or_404(Post, pk=serializer.data.get('related_post'))
        return Comment.objects.create(content=serializer.data.get('content'),
                                      creator=self.scope['user'], related_post=post)
