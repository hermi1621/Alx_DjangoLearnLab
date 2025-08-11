Author.objects.get(name=author_name)
from .models import Author, Book

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books
