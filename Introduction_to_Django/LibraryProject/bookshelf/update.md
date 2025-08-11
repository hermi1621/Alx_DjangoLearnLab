# Update a Book Title

To update the title of a book from "1984" to "Nineteen Eighty-Four":

```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

print(book.title)
# Expected output: Nineteen Eighty-Four

---

### `delete.md`

```md
# Delete a Book

To delete the book with title "Nineteen Eighty-Four":

```python
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
books = Book.objects.all()
print(books)
# Expected output: <QuerySet []>

---

Would you like me to provide a combined `CRUD_operations.md` as well, or help you push these files step-by-step on GitHub?

