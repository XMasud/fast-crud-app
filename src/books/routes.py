from fastapi import APIRouter, status

from src.books.schemas import Book

books_router = APIRouter()

@books_router.get("/", response_model=list[Book])
async def read_books(skip: int = 0, limit: int = 100) -> list[Book]:
    return await Book.query.skip(skip).limit(limit)

@books_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book_data: Book):
    return {
        "title": book_data.title,
        "author": book_data.author,
        "status": "New Book created successfully!"
    }