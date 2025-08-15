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
        from django.db import models

# Author model: represents a writer
class Author(models.Model):
    name = models.CharField(max_length=100)  # Stores the author's name

    def __str__(self):
        return self.name


# Book model: represents a book written by an author
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book title
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE
    )  # One-to-many: one author can have many books

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

