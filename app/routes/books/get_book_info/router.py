from fastapi import APIRouter
from app.db.models.book.interface import BookInterFace
from app.db.models.book_author_association.interface import BookAuthorAssociationInterFace
from app.routes.books.get_book_info.schema import SBookGet
from app.routes.exceptions import *

router = APIRouter()

@router.get("/get_all")
async def get_all_books() -> list[SBookGet]:
    return await BookInterFace.find_all()


@router.get("/get_info/{book_id}")
async def get_book_by_id(book_id: int) -> SBookGet | dict:
    result : SBookGet = await BookInterFace.find_full_data(id=book_id)
    if result is None:
        return {'message': f'Книга с ID {book_id} не найдена!'}
    return result


@router.get("/get_info/{book_id}")
async def get_book_by_id(book_id: int) -> SBookGet | dict:
    result = await BookInterFace.find_full_data(id=book_id)
    if result is None:
        return {'message': f'Книга с ID {book_id} не найдена!'}
    return result


@router.get("/get_count_book/{book_id}")
async def get_book_by_id(book_id: int) -> int:
    result = await BookAuthorAssociationInterFace.find_all(book_id=book_id)
    return len(result)