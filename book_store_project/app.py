from lib.book_store_repository import *
from lib.database_connection import *
from lib.book_store import *


connection = DatabaseConnection()
connection.connect()

connection.seed("seeds/book_store.sql")

books_repository = BookRepository(connection)

books = books_repository.all()

for book in books:
    print(book)