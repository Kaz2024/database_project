from lib.book_store import *

def test_bool_store_constructs():
    books = BookStore("title", "author_name")
    assert books.title == "title"
    assert books.author_name == "author_name"

def test_books_are_equal():
    book1 = BookStore("title", "author_name")
    book2 = BookStore("title", "author_name")
    assert book1 == book2

def test_format():
    books = BookStore("title","author_name")
    assert str(books) == "title - author_name"