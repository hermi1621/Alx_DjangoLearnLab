Checks for “List all books in a library.” task
from .models import Book

def list_all_books():
    return Book.objects.all()
 Checks for “Query all books by a specific author.” task
def books_by_author(author_name):
    return Book.objects.filter(author__first_name=author_name)
Checks for “Retrieve the librarian for a library.” task
from .models import Librarian

def get_librarian(library_id):
    return Librarian.objects.get(id=library_id)
