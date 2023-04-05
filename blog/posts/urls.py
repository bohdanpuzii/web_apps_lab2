from django.urls import path
from django.urls import re_path

from . import views
from . import ws_views

urlpatterns = [
    path('posts/<str:username>/', views.PostListView.as_view()),
    path('posts/create', views.PostCreateView.as_view()),
    path('posts/<int:pk>/delete', views.PostDeleteView.as_view()),
    path('comment/', views.CommentCreateView.as_view()),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view()),
    path('comment/<int:pk>', views.CommentRetrieveView.as_view()),
]

ws_patterns = [
    re_path(r"^ws/$", ws_views.PostListConsumer.as_asgi())
]
