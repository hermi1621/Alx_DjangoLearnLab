from django.urls import path
from .views import BookListCreateAPIView

urlpatterns = [
    path('api/books/', BookListCreateAPIView.as_view(), name='book_list_create'),
]
from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
