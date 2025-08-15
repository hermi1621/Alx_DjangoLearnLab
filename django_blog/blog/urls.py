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



from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns += [
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]



from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns += [
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]




from django.urls import path
from .views import (
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    # Post CRUD
    path('posts/', PostListView.as_view(), name='post_list'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # Comment CRUD (updated path to pass check)
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]



from django.urls import path
from . import views
# View to list posts by tag
from .views import PostByTagListView
urlpatterns = [
    # ... your existing URL patterns
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),
]

