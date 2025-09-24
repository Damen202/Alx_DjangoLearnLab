from django.urls import path
from .views import BookDeleteView, BookCreateView, BookDetailView, BookListView, BookUpdateView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<ink:pk>/', BookDeleteView.as_view(), name='book-delete'),
    path('books/<ink:pk>/', BookCreateView.as_view(), name='book-create'),
    path('books/<ink:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<ink:pk>/', BookUpdateView.as_view(), name='book-update'),
]