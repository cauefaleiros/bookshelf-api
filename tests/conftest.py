import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.config.database import Base, get_db
from app.main import app
from app.db.models.book_model import Book

SQLALCHEMY_DATABASE_URL = "sqlite:///.//test.db"

@pytest.fixture
def db_session():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Base.metadata.create_all(bind=engine)

    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    yield session

    session.close()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(db_session):
    try:
        yield db_session
    finally:
        db_session.close()

app.dependecy_overrides[get_db] = override_get_db

with TestClient(app) as test_client:
    yield test_client

app.dependecy_overrides.clear()

