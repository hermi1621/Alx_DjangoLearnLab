from .models import Author, Book, Library

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)  # This matches the check
    books = Book.objects.filter(author=author)
    return books

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)  # Retrieves the library object
    librarian = library.librarian  # Assumes a OneToOne or ForeignKey field
    return librarian
