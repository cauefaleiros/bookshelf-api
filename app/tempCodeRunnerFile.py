import sys
import os
from fastapi import FastAPI
from app.config.database import engine, Base
from app.api.v1.endpoints.book_endpoint import app as book_router

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bookshelf API", version="1.0.0")

app.include_router(book_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Bookshelf API is running!"}

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="127.0.0.1", port=8000)