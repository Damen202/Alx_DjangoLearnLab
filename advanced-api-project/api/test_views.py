# /api/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Book
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()
        self.client.login(username="testuser", password="testpass")

        # Create some sample books
        self.book1 = Book.objects.create(title="The Hobbit", author="Tolkien", published_date="1937-09-21")
        self.book2 = Book.objects.create(title="1984", author="Orwell", published_date="1949-06-08")

        self.list_url = reverse("book-list")  # from your urls.py
        self.create_url = reverse("book-create")

    # --- CRUD Tests ---
    def test_create_book(self):
        data = {"title": "Django for APIs", "author": "William Vincent", "published_date": "2020-01-01"}
        response = self.client.post(self.create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "Django for APIs")

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_book(self):
        url = reverse("book-update", args=[self.book1.id])
        data = {"title": "The Hobbit (Updated)", "author": "Tolkien", "published_date": "1937-09-21"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "The Hobbit (Updated)")

    def test_delete_book(self):
        url = reverse("book-delete", args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # --- Filtering / Searching / Ordering Tests ---
    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url, {"author": "Tolkien"})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Tolkien")

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url, {"search": "1984"})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "1984")

    def test_order_books_by_title_desc(self):
        response = self.client.get(self.list_url, {"ordering": "-title"})
        titles = [book["title"] for book in response.data]
        self.assertEqual(titles, sorted(titles, reverse=True))

    # --- Permissions ---
    def test_unauthenticated_user_cannot_create_book(self):
        client = APIClient()  # new client without login
        data = {"title": "Unauthorized Book", "author": "Anon", "published_date": "2022-01-01"}
        response = client.post(self.create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # or 401 if using JWT