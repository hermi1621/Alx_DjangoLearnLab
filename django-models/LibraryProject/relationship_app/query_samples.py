from .models import Library, Book, Librarian

# List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()  # Assuming 'books' is the related_name in Book model's ForeignKey

# Query all books by a specific author
def books_by_author(author):
    return Book.objects.filter(author=author)

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian  # Assuming OneToOneField with related_name='librarian'
