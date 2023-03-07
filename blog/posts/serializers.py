from rest_framework import serializers
from .models import Post, Comment


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'created_at', 'title', 'content', 'comments', 'author')


class PostCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = self.context['request'].user
        post = Post.objects.create(title=validated_data.get('title'), content=validated_data.get('content'), author=user)
        return post

    class Meta:
        model = Post
        fields = ('title', 'content', )


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('content', 'related_post')

    def create(self, validated_data):
        user = self.context['request'].user
        comment = Comment.objects.create(content=validated_data.get('content'), creator=user,
                                         related_post=validated_data.get('related_post'))
        return comment


class CommentRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
