from fastapi import APIRouter, Depends
from app.db.models.book.interface import BookInterFace
from app.routes.books.get_book_info.rb import RBBook
from app.routes.books.get_book_info.schema import SBookGet
from app.routes.exceptions import *

router = APIRouter()

@router.get("/get_all")
async def get_all_books(request_body: RBBook = Depends()) -> list[SBookGet]:
    return await BookInterFace.find_all(**request_body.to_dict())


@router.get("/get_info/{book_id}")
async def get_student_by_id(book_id: int) -> SBookGet | dict:
    result = await BookInterFace.find_full_data(id=book_id)
    if result is None:
        return {'message': f'Книга с ID {book_id} не найдена!'}
    return result


@router.get("/get_by_filter")
async def get_student_by_filter(request_body: RBBook = Depends()) -> RBBook | dict:
    result = await BookInterFace.find_one_or_none(**request_body.to_dict())
    if result is None:
        return {'message': f'Книга с указанными параметрами не найдена!'}
    return result
  