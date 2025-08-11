from .models import Author, Book

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)  # must be exactly this line
    books = Book.objects.filter(author=author)
    return books
