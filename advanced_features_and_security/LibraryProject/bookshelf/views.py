from django.shortcuts import render
from .models import Book
from .forms import SearchForm

def book_search(request):
    form = SearchForm(request.GET or None)
    books = Book.objects.none()
    if form.is_valid():
        query = form.cleaned_data['query']
        # Safe ORM filter with parameterization
        books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})
