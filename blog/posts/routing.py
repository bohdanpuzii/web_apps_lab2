from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path("ws/posts/", consumers.PostConsumer.as_asgi()),
    re_path("ws/comments/", consumers.CommentConsumer.as_asgi())
]
