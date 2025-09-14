from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .models import Book
from .forms import BookForm, BookSearchForm
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import ExampleForm, BookForm

def home(request):
    return HttpResponse("Welcome to the Bookshelf app!")

@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    # logic for creating a book
    return render(request, "bookshelf/book_form.html")

@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # logic for editing a book
    return render(request, "bookshelf/book_form.html", {"book": book})

@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("book_list")


@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    form = BookSearchForm(request.GET or None)
    qs = Book.objects.all()
    # Cleaned & validated input via form
    if form.is_valid() and form.cleaned_data.get("q"):
        q = form.cleaned_data["q"]
        # Use ORM with parameterization (no string interpolation)
        qs = qs.filter(Q(title__icontains=q) | Q(author__icontains=q))

    paginator = Paginator(qs, 10)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    return render(request, "bookshelf/book_list.html", {"page_obj": page_obj, "form": form})

@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/book_form.html", {"form": form})

@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/book_form.html", {"form": form, "book": book})

@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})

@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/book_form.html", {"form": form})


def example_view(request):
    """Demo view using ExampleForm"""
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Example processing
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data.get("message", "")
            return render(
                request,
                "bookshelf/example_success.html",
                {"name": name, "email": email, "message": message},
            )
    else:
        form = ExampleForm()

    return render(request, "bookshelf/example_form.html", {"form": form})