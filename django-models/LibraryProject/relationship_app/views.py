from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library  # ✅ Added this import

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
