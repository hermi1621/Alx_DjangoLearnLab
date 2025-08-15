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

