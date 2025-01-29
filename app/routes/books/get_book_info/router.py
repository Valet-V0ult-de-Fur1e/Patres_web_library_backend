from fastapi import APIRouter
from app.db.models.book.interface import BookInterFace
from app.db.models.book.model import BookModel
from app.db.models.book_author_association.interface import BookAuthorAssociationInterFace
from app.routes.books.get_book_info.schema import SBookGet
from app.routes.exceptions import *

router = APIRouter()

@router.get("/get_all")
async def get_all_books():
    data = await BookInterFace.find_all()
    return data


@router.get("/get_info/{book_id}")
async def get_book_by_id(book_id: int) -> SBookGet | dict:
    result = await BookInterFace.find_full_data(id=book_id)
    if result is None:
        return {'message': f'Книга с ID {book_id} не найдена!'}
    return result


@router.get("/get_count_book_in_use/{book_id}")
async def get_count_book_in_use(book_id: int) -> int:
    result = await BookAuthorAssociationInterFace.find_all(book_id=book_id)
    return len(result)


@router.get("/get_count_book_not_in_use/{book_id}")
async def get_count_book_not_in_use(book_id: int) -> int:
    result = await BookAuthorAssociationInterFace.find_all(book_id=book_id)
    count_books:BookModel = await BookInterFace.find_one_or_none_by_id(data_id=book_id)
    return count_books.count_copies - len(result)