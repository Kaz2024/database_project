from lib.book_store import *
from lib.book_store_repository import *


def test_list_all_books(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    result = repository.all()
    assert result == [
            BookStore('Nineteen Eighty-Four', 'George Orwell'),
            BookStore('Mrs Dalloway', 'Virginia Woolf'),
            BookStore('Emma', 'Jane Austen'),
            BookStore('Dracula', 'Bram Stoker'),
            BookStore('The Age of Innocence', 'Edith Wharton')]