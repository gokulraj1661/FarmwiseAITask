from __init__ import app,db
import unittest
import models
import base64

class test_get_all_books(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    

    def test_index(self):
          try:
            # Make a GET request to the endpoint
            credentials = base64.b64encode(b"Username:password").decode('utf-8')
            response = self.app.get('/getall',headers={'Authorization': 'Basic ' + credentials})
            statuscode = response.status_code
            # Check the response status code
            self.assertEqual(statuscode, 200)

          except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    def test_get_by_isbn_existing_book(self):
        try:
        # Insert a sample book into the database
            sample_book = models.Book(title='Witcher', author='Henry',isbn='100',price='200',quantity='2')
            with app.app_context():
                db.session.add(sample_book)
                db.session.commit()

        # Make a GET request to the endpoint with the existing ISBN
            credentials = base64.b64encode(b"Username:password").decode('utf-8')
            response = self.app.get('/getbyisbn/100',headers={'Authorization': 'Basic ' + credentials})

            print(response.json)
        # Check the response status code
            self.assertEqual(response.status_code, 200)
            # expected_data = {'title': 'Witcher', 'author': 'Henry', 'isbn':'100', 'price':'200','quantity':'2'}
        
            book_data = response.get_json()
            self.assertEqual(book_data['title'], 'Witcher')
            self.assertEqual(book_data['author'], 'Henry')
            self.assertEqual(book_data['isbn'], '100')
            self.assertEqual(book_data['price'], 250)
            self.assertEqual(book_data['quantity'], 5)


        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
      
    def test_add_book(self):
        try:
            # Make a POST request to add a book
            credentials = base64.b64encode(b"Username:password").decode('utf-8')
            response = self.app.post('/add', json={'title': 'Harry Porter', 'author': 'Hary', 'isbn': '102', 'price': 250, 'quantity': 7}, headers={'Authorization': 'Basic ' + credentials})

            # Check the response status code
            self.assertEqual(response.status_code, 200)

            # Check the returned data
            book_data = response.get_json()
            self.assertEqual(book_data['title'], 'Harry Porter')
            self.assertEqual(book_data['author'], 'Hary')
            self.assertEqual(book_data['isbn'], '102')
            self.assertEqual(book_data['price'], 250)
            self.assertEqual(book_data['quantity'], 7)

        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")


            
    def test_update_book(self):
        try:
            # Insert a sample book into the database
            sample_book = models.Book(title='Witcher', author='Henry', isbn='100', price=200, quantity=2)
            with app.app_context():
                db.session.add(sample_book)
                db.session.commit()
            
            # Make a PUT request to update the book
            credentials = base64.b64encode(b"Username:password").decode('utf-8')
            updated_data = {'title': 'Witcher', 'author': 'Henry', 'isbn':100,'price': 250, 'quantity': 5}
            response = self.app.put('/update/7 ', json=updated_data, headers={'Authorization': 'Basic ' + credentials})

            # print(response)
            # Check the response status code
            self.assertEqual(response.status_code, 200)

            # Check the returned data
            updated_book_data = response.get_json()
            self.assertEqual(updated_book_data['title'], 'Witcher')
            self.assertEqual(updated_book_data['author'], 'Henry')
            self.assertEqual(updated_book_data['isbn'], '100')  # ISBN should remain the same
            self.assertEqual(updated_book_data['price'], 250)
            self.assertEqual(updated_book_data['quantity'], 5)

        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    '''
    def test_delete_book_by_id(self):
        try:
            # Insert a sample book into the database
            sample_book = models.Book(title='Polar', author='srk', price=270, isbn=120, quantity=1)
            with app.app_context():
                db.session.add(sample_book)
                db.session.commit()

            # Make a DELETE request to delete the book by ID
            credentials = base64.b64encode(b"Username:password").decode('utf-8')
            p
            book_id = sample_book.id  # Assuming the Book model has an 'id' attribute

            response = self.app.delete(f'/delete/120', headers={'Authorization': 'Basic ' + credentials})

            print(response)

            # Check the response status code
            self.assertEqual(response.status_code, 200)

            # Ensure the book is no longer in the database
            with app.app_context():
                deleted_book = models.Book.query.get(book_id)
                self.assertIsNone(deleted_book, "The book should be deleted from the database.")

        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
'''

if __name__ == '__main__':
    unittest.main()