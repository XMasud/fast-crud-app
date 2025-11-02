from fastapi import FastAPI, status
from typing import Optional

from schemas import Book

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/greet")
async def say_hello(name: Optional[str] = "User", age: int = 1) -> dict:
    return {"message": f"Hello {name}, you are {age} years old"}

@app.get("/books", response_model=list[Book])
async def read_books(skip: int = 0, limit: int = 100) -> list[Book]:
    return await Book.query.skip(skip).limit(limit)

@app.post("/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_data: Book):
    return {
        "title": book_data.title,
        "author": book_data.author,
        "status": "New Book created successfully!"
    }

@app.get("/get_headers")
async def het_headers():
    return {}
