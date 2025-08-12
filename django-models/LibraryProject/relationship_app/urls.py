from django.urls import path
from . import views

urlpatterns = [
    # Existing URL patterns...

    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    # You can also add delete_book if needed
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]
