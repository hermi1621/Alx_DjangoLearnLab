from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Registration
    path('register/', views.register, name='register'),  # ✅ views.register

    # Login
    path(
        'login/',
        LoginView.as_view(template_name='relationship_app/login.html'),  # ✅ LoginView.as_view(template_name=...)
        name='login'
    ),

    # Logout
    path(
        'logout/',
        LogoutView.as_view(template_name='relationship_app/logout.html'),  # ✅ LogoutView.as_view(template_name=...)
        name='logout'
    ),
]
