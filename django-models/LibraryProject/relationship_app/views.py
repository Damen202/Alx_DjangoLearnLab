from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library


# Function-based view: List all books
def book_list(request):
    books = Book.objects.select_related('author').all()
    return render(request, "list_books.html", {"books": books})

# Class-based view: Show library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
