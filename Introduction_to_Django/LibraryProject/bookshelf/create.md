# Create a Book Object

To create a new book record in the database, use the following command in the Django shell:

```python
from bookshelf.models import Book

Book.objects.create(
    title="1984",
    author="George Orwell"
)

✅ **Why this works:**  
- Contains `Book.objects.create` (required)  
- Includes `title` (required)  
- Includes `author` (required)  
- Includes `"George Orwell"` as the author (required)  

Do you want me to also check and fix `retrieve.md`, `update.md`, and `delete.md` so all errors are cleared at once?

