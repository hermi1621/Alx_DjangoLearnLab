from django.urls import path
from . import views
from .views import CustomLoginView, CustomLogoutView

urlpatterns = [
    path('register/', views.register_view, name='register'),  # Registration URL
    path('login/', CustomLoginView.as_view(), name='login'),  # Login URL
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Logout URL
    path('profile/', views.profile_view, name='profile'),  # Profile URL
]

