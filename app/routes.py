from flask import request, jsonify
from __init__ import app, db
from app.models import Book
from app.schemas import book_schema, books_schema

@app.route('/add',methods=['POST'])
def add_book():
    title=request.json['title']
    author=request.json['author']
    isbn=request.json['isbn']
    price=request.json['price']
    quantity=request.json['quantity']

    new_Book=Book(title,author,isbn,price,quantity)
    db.session.add(new_Book)
    db.session.commit()
    return book_schema.jsonify(new_Book)

@app.route('/getall',methods=['GET'])
def get_all_books():
    all_books=Book.query.all()
    result=books_schema.dump(all_books)
    return jsonify(result)

@app.route('/getbyisbn/<isbn>',methods=['GET'])
def get_by_isbn(isbn):
    book=Book.query.filter_by(isbn=isbn).first()
    if book:
        return book_schema.jsonify(book)
    else:
        return jsonify({"message": "Book not found"}), 404

@app.route('/update/<id>',methods=['PUT'])
def update_by_id(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({"message": "Book not found"}), 404

    # Update book properties based on the JSON data in the request
    book.title = request.json.get('title', book.title)
    book.author = request.json.get('author', book.author)
    book.isbn = request.json.get('isbn', book.isbn)
    book.price = request.json.get('price', book.price)
    book.quantity = request.json.get('quantity', book.quantity)

    db.session.commit()
    return book_schema.jsonify(book)
    
@app.route('/delete/<id>',methods=['DELETE'])
def delete_by_id(id):
    book = Book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": f"Book with ID {id} has been deleted"})
    else:
        return jsonify({"message": "Book not found"}), 404
