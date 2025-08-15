from django.db import models
from django.contrib.auth.models import User

# Post model for blog posts
class Post(models.Model):
    title = models.CharField(max_length=200)                 # Post title
    content = models.TextField()                             # Post content
    published_date = models.DateTimeField(auto_now_add=True) # Automatically set when created
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'  # One user can have many posts
    )

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User

from .models import Post  # Ensure Post is imported

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)  # Many-to-one
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"


