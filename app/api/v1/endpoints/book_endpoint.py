from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.book_schema import BookCreate, BookUpdate, BookResponse
from app.repositories.book_repository import create_book, get_books, get_book_by_id, update_book, delete_book


app = APIRouter()

@app.get("/books", response_model=list[BookResponse], status_code=status.HTTP_200_OK)
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = get_books(db, skip=skip, limit=limit)
    return books

@app.get("/books/{book_id}", response_model=BookResponse, status_code=status.HTTP_200_OK)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = get_book_by_id(db, book_id)
    if db_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found"
        )
    return db_book

@app.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = create_book(db, book)
    return db_book

@app.put("/books/{book_id}", response_model=BookResponse, status_code=status.HTTP_200_OK)
def update_existing_book(book_id: int, book_update: BookUpdate, db: Session = Depends(get_db)):
    db_book = update_book(db, book_id, book_update)
    if db_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found"
        )
    return db_book

@app.delete("/books/{book_id}", status_code=status.HTTP_200_OK)
def delete_existing_book(book_id: int, db: Session = Depends(get_db)):
    success = delete_book(db, book_id) 
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found"
        )
    return {"message": f"Book with id {book_id} deleted successfully"}