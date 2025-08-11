# Retrieve a Book

To retrieve a book with the title "1984":

```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
print(book.author)

---

Do you want me to also update **`create.md`**, **`update.md`**, and **`delete.md`** so all errors are fixed in one go? That way you won’t need to fix them one by one.

