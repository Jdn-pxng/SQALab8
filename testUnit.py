#jetsadaphon bokprakhon 653380014-1 sec.1
#Lab8

import pytest
from main import User
from main import Book

def test_register_user(db_session):
    newUser = User(username = "USName01",fullname = "FName01",has_book = True)
    db_session.add(newUser)
    db_session.commit()

    User = db_session.query(User).filter_by(username="FName01").first()
    assert User is not None
    assert User.username == "FName01"

def test_remove_user(db_session):
    newUser2 = User(username = "FName02",fullname = "FName02",has_book = True)
    db_session.add(newUser2)
    db_session.commit()

    db_session.delete(newUser2)
    db_session.commit()

    DeletedUser = db_session.query(User).filter_by(username="FName02").first()
    assert DeletedUser is None

def test_register_book(db_session):
    newBook = Book(title = "colorful",firstauthor = "HP_lovecraft",isbn = "isbn001")
    db_session.add(newBook)
    db_session.commit()

    Book = db_session.query(Book).filter_by(title="colorful").first()
    assert Book is not None
    assert Book.title == "colorful"

def test_remove_user(db_session):
    newBook2 = User(title = "cathulu",firstauthor = "HP_lovecraft",isbn = "isbn002")
    db_session.add(newBook2)
    db_session.commit()

    db_session.delete(newBook2)
    db_session.commit()

    DeletedBook = db_session.query(Book).filter_by(title="cathulu").first()
    assert DeletedBook is None


