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

### How to do this in GitHub web UI:

1. Go to your repo → `LibraryProject/bookshelf/`
2. Click **Add file → Create new file**
3. Name it: `delete.md`
4. Paste the above content inside the editor
5. Scroll down, add commit message: `add delete.md for Book model CRUD`
6. Commit the file directly to main branch (or your branch)

---

Let me know if you want me to create the other `.md` files similarly or prepare everything in one go!
