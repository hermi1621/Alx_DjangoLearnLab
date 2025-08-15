from django.urls import path
from . import views
from .views import CustomLoginView, CustomLogoutView

urlpatterns = [
    path('register/', views.register_view, name='register'),  # Registration URL
    path('login/', CustomLoginView.as_view(), name='login'),  # Login URL
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Logout URL
    path('profile/', views.profile_view, name='profile'),  # Profile URL
]



from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,
    register_view, CustomLoginView, CustomLogoutView, profile_view
)

urlpatterns = [
    # Authentication URLs
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),

    # Blog Post CRUD URLs (singular 'post/' as required)
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    
    # Optional: Post list view (can keep plural for listing)
    path('posts/', PostListView.as_view(), name='post_list'),
]
