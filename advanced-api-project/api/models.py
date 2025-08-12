from django.db import models

class Author(models.Model):
    # Author's name
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    # Book title
    title = models.CharField(max_length=200)
    # Year published
    publication_year = models.IntegerField()
    # Link to author (one-to-many)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
