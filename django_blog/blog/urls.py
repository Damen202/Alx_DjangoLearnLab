# blog/urls.py

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post routes (existing)
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # comment routes
    path('posts/<int:post_pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('posts/<int:post_pk>/comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('posts/<int:post_pk>/comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]

