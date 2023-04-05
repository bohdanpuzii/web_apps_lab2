from django.urls import path

from . import views

urlpatterns = [
    path('posts/<str:username>/', views.PostListView.as_view()),
    path('posts/create', views.PostCreateView.as_view()),
    path('posts/<int:pk>/delete', views.PostDeleteView.as_view()),
    path('comment/', views.CommentCreateView.as_view()),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view()),
    path('comment/<int:pk>', views.CommentRetrieveView.as_view()),
]

