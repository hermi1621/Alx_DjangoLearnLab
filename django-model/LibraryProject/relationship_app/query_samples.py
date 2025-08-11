from .models import Author, Book, Library

# Query all books by a specific author
def get_books_by_author(author_name):
    # This exact line is required for the check
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books
