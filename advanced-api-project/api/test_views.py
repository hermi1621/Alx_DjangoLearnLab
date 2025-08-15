from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITests(APITestCase):

    def setUp(self):
        # Create users
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.admin_user = User.objects.create_superuser(username="admin", password="adminpass")

        # Create an author
        self.author = Author.objects.create(name="John Doe")

        # Create some books
        self.book1 = Book.objects.create(
            title="Book One", author=self.author, publication_year=2020
        )
        self.book2 = Book.objects.create(
            title="Book Two", author=self.author, publication_year=2021
        )

        # Endpoints
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book1.id])
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", args=[self.book1.id])
        self.delete_url = reverse("book-delete", args=[self.book1.id])

    def test_list_books(self):
        """Test GET /books/ returns list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_filter_books_by_year(self):
        """Test filtering books by publication_year"""
        response = self.client.get(self.list_url, {"publication_year": 2021})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(b["publication_year"] == 2021 for b in response.data))

    def test_search_books_by_title(self):
        """Test searching books by title"""
        response = self.client.get(self.list_url, {"search": "Book One"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Book One" in b["title"] for b in response.data))

    def test_order_books_by_title(self):
        """Test ordering books by title"""
        response = self.client.get(self.list_url, {"ordering": "title"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [b["title"] for b in response.data]
        self.assertEqual(titles, sorted(titles))

    def test_create_book_authenticated(self):
        """Test creating a book as authenticated user"""
        self.client.login(username="testuser", password="pass1234")
        data = {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2022
        }
        response = self.client.post(self.create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Test creating a book without authentication fails"""
        data = {
            "title": "Unauthorized Book",
            "author": self.author.id,
            "publication_year": 2023
        }
        response = self.client.post(self.create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """Test updating a book as authenticated user"""
        self.client.login(username="testuser", password="pass1234")
        data = {"title": "Updated Book"}
        response = self.client.patch(self.update_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_delete_book_authenticated(self):
        """Test deleting a book as authenticated user"""
        self.client.login(username="testuser", password="pass1234")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_delete_book_unauthenticated(self):
        """Test deleting a book without authentication fails"""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
