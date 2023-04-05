from django.urls import re_path
from . import consumers, views

websocket_urlpatterns = [
    re_path("ws/posts/", consumers.PostListConsumer.as_asgi()),
    #re_path("ws/posts/delete/", consumers.PostDeleteConsumer.as_asgi())
]
