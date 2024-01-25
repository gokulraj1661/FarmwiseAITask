from __init__ import ma
from app.models import Book

class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'author', 'isbn', 'price', 'quantity')

book_schema = BookSchema()
books_schema = BookSchema(many=True)
