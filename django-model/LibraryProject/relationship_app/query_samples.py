from .models import Author, Book, Library

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)  # Exact string needed here
    books = Book.objects.filter(author=author)
    return books

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)  # Needed for librarian retrieval
    return library.librarian
