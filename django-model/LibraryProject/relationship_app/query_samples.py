from .models import Author, Book, Library

# Query all books by a specific author
def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)  # exact required line
    books = Book.objects.filter(author=author)
    return books

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # assumes OneToOneField relationship
    return librarian
