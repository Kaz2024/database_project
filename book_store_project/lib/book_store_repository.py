from lib.book_store import *

class BookRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM books') 
        books = []
        for row in rows:
            book = BookStore(row['title'],row['author_name'])
            books.append(book)
        return books
    