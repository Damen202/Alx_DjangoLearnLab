# Retrieve Operation

```python
from bookshelf.models import Book
books = Book.objects.get()
books
# <QuerySet [<Book: 1984 by George Orwell (1949)>]>