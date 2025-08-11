from .models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

