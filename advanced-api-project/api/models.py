from django.db import models

class Author(models.Model):
    # Stores the author's name
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=200)
    # Publication year as integer
    publication_year = models.IntegerField()
    # Link to author - one author to many books
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
