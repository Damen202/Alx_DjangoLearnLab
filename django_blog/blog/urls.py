from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Post URLs
    path('post/', views.PostListView.as_view(), name='list'),
    path('post/new/', views.PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),

    # Comment URLs
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    #tags and search URLs
    path('search/', views.search_posts, name='post-search'),
    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts-by-tag'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts-by-tag'),
]
