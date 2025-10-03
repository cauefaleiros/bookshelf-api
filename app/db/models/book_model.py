from sqlalchemy import Column, Integer, String, Boolean, Text
from app.config.database import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    sinopse = Column(Text)
    genre = Column(String(100))
    writer = Column(String(100), nullable=False)
    pages = Column(Integer)
    edition = Column(Integer)
    publication_year = Column(Integer)
    available  = Column(Boolean, default=True)