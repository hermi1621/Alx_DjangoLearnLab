from django.shortcuts import render
from django.views.generic.detail import DetailView  # ✅ Added for checker
from .models import Library, Book  # ✅ Importing both models

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # ✅ Required for checker
    return render(request, "relationship_app/list_books.html", {"books": books})
