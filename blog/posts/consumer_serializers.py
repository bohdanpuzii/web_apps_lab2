from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=256)
    content = serializers.CharField(max_length=256)
    comments = serializers.IntegerField(required=False)
    author = serializers.IntegerField(required=False)

    class Meta:
        model = Post
        fields = ('id', 'created_at', 'title', 'content', 'comments', 'author')

    # def create(self, validated_data):
    #     print(self.__slots__)
    #     user = self.scope['user']
    #     post = Post.objects.create(title=validated_data.get('title'), content=validated_data.get('content'), author=user)
    #     return post

