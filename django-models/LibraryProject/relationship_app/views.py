from django.shortcuts import render, get_object_or_404
from .models import Book, Library
from django.views.generic import DetailView

# Function-based view for listing all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view for displaying library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
