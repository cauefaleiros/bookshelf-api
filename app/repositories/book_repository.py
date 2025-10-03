from sqlalchemy.orm import Session
from app.db.models.book_model import Book
from app.schemas.book_schema import BookCreate, BookUpdate
from typing import List, Optional

def create_book(db: Session, book: BookCreate) -> Book:
    db_book = Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, skip: int = 0, limit: int = 100) -> List[Book]:
    return db.query(Book).offset(skip).limit(limit).all()

def get_book_by_id(db: Session, book_id: int) -> Optional[Book]:
    return db.query(Book).filter(Book.id == book_id).first()

def update_book(db: Session, book_id: int, book_update: BookUpdate) -> Optional[Book]:
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        return None
    for key, value in book_update.model_dump(exclude_unset=True).items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int) -> bool:
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        return False
    db.delete(db_book)
    db.commit()
    return True
