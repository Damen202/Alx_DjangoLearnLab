from django.urls import path
from .views import BookDeleteView, BookCreateView, BookDetailView, BookListView, BookUpdateView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/delete/<ink:pk>/', BookDeleteView.as_view(), name='book-delete'),
    path('books/create/<ink:pk>/', BookCreateView.as_view(), name='book-create'),
    path('books/detail/<ink:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/update/<ink:pk>/', BookUpdateView.as_view(), name='book-update'),
]