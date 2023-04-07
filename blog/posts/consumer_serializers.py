from rest_framework import serializers
from .models import Post, Comment


class PostListSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=256)
    content = serializers.CharField(max_length=256)

    class Meta:
        model = Post
        fields = ('id', 'created_at', 'title', 'content', 'comments', 'author')


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=256)
    content = serializers.CharField(max_length=256)
    comments = serializers.IntegerField(required=False)
    author = serializers.IntegerField(required=False)

    class Meta:
        model = Post
        fields = ('id', 'created_at', 'title', 'content', 'comments', 'author')


class CommentSerializer(serializers.ModelSerializer):
    content = serializers.CharField(max_length=256)
    creator = serializers.IntegerField(required=False)

    class Meta:
        model = Comment
        fields = ('id', 'created_at', 'creator', 'content', 'related_post')


class CommentRetrieveSerializer(serializers.ModelSerializer):
    content = serializers.CharField(max_length=256)
    #creator = serializers.IntegerField(required=False)

    class Meta:
        model = Comment
        fields = ('id', 'created_at', 'creator', 'content', 'related_post')