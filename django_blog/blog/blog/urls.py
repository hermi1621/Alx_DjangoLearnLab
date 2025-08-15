from django.urls import path
from . import views
from .views import CustomLoginView, CustomLogoutView

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),
]



from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,
    register_view, CustomLoginView, CustomLogoutView, profile_view
)

urlpatterns = [
    # Authentication
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),

    # CRUD for posts
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),



    from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,
    register_view, CustomLoginView, CustomLogoutView, profile_view
)

urlpatterns = [
    # Authentication
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),

    # CRUD for posts (updated to match exact check paths)
    path('posts/', PostListView.as_view(), name='post_list'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),              # singular 'post/new/'
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),  # singular 'post/<int:pk>/update/'
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # singular 'post/<int:pk>/delete/'
]

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



from .views import SearchResultsView, PostsByTagView

urlpatterns += [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('tags/<slug:tag_slug>/', PostsByTagView.as_view(), name='posts_by_tag'),
]

