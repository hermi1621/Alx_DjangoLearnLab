from .models import Author, Book, Librarian

# Create an author
author = Author.objects.create(name="George Orwell", birth_date="1903-06-25")

# Create a book for the author
book = Book.objects.create(title="Nineteen Eighty-Four", author=author)

# Create a librarian
librarian = Librarian.objects.create(name="John Doe", library="Central Library")

# Example queries
all_books = Book.objects.all()
books_by_orwell = Book.objects.filter(author__name="George Orwell")
