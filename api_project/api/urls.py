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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing list view path
    path('books/', BookList.as_view(), name='book-list'),

    # Include all routes created by the router for BookViewSet
    path('', include(router.urls)),
]

