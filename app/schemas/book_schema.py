from pydantic import BaseModel, ConfigDict
from typing import Optional


class BookBase(BaseModel):
    title: str
    sinopse: Optional[str] = None
    genre: Optional[str] = None
    writer: str
    pages: Optional[int] = None
    edition: Optional[int] = None
    publication_year: Optional[int] = None
    available: Optional[bool] = None

class BookCreate(BookBase):
    title: str
    writer: str

class BookUpdate(BaseModel):
    title: Optional[str] = None
    sinopse: Optional[str] = None
    genre: Optional[str] = None
    writer: Optional[str] = None
    pages: Optional[int] = None
    edition: Optional[int] = None
    publication_year: Optional[int] = None
    available: Optional[bool] = None

class BookResponse(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)