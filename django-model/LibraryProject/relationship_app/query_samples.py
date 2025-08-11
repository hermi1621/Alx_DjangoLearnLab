from .models import Library, Book, Author, Librarian

# List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian
