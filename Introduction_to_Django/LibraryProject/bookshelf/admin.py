from django.contrib import admin
from .models import Book

# Register the Book model to appear in admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # Columns to display
    list_filter = ("publication_year",)                      # Sidebar filters
    search_fields = ("title", "author")                      # Search box for title and author
