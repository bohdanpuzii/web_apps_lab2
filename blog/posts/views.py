from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment, User
from .serializers import PostListSerializer, PostCreateSerializer, CommentCreateSerializer, CommentRetrieveSerializer
from .permissions import IsOwnerOrSuperuser, IsOwnerOrSuperuserOrPostOwner


class PostListView(ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        posts = Post.objects.filter(author=user)
        return posts


class PostCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = PostCreateSerializer


class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrSuperuser, )


class CommentCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CommentCreateSerializer


class CommentDeleteView(DestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = (IsOwnerOrSuperuserOrPostOwner, )


class CommentRetrieveView(RetrieveAPIView):
    serializer_class = CommentRetrieveSerializer
    queryset = Comment.objects.all()

