import django_tables2 as tables
from books.models import Book

class BookTable(tables.Table):
    class Meta:
        model = Book
        
        attrs = {"class": "table-auto"}