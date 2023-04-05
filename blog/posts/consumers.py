from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    DeleteModelMixin,
)

from .models import Post
from .consumer_serializers import PostSerializer
from .consumer_permissions import PostPermissions


class PostListConsumer(GenericAsyncAPIConsumer, ListModelMixin, DeleteModelMixin, CreateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (PostPermissions,)
    lookup_field = 'pk'

    def get_queryset(self, **kwargs):
        if kwargs.get('action') == 'list':
            user = get_object_or_404(User, username=kwargs.get('username'))
            posts = Post.objects.filter(author=user)
            return posts
        return Post.objects.all()

    def perform_create(self, serializer, **kwargs):
        return Post.objects.create(title=serializer.data.get('title'), content=serializer.data.get('content'),
                                   author=self.scope['user'])
