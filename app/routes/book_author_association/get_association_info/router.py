from fastapi import APIRouter, Depends
from app.db.models.book_author_association.interface import BookAuthorAssociationInterFace
from app.routes.book_author_association.get_association_info.rb import RBBookAuthorAssociation
from app.routes.book_author_association.get_association_info.schema import SBookAuthorAssociationGet
from app.routes.exceptions import *
router = APIRouter()

@router.get("/get_all")
async def get_all_associations(request_body: RBBookAuthorAssociation = Depends()) -> list[SBookAuthorAssociationGet]:
    return await BookAuthorAssociationInterFace.find_all(**request_body.to_dict())


@router.get("/get_by_filter")
async def get_association_by_filter(request_body: RBBookAuthorAssociation = Depends()) -> SBookAuthorAssociationGet | dict:
    result = await BookAuthorAssociationInterFace.find_one_or_none(**request_body.to_dict())
    if result is None:
        return {'message': f'Связь с указанными параметрами не найдена!'}
    return result


@router.get("/get_info_by_author_id/{author_id}")
async def get_association_by_author_id(author_id: int) -> SBookAuthorAssociationGet | dict:
    result = await BookAuthorAssociationInterFace.find_one_or_none_by_id(author_id=author_id)
    if result is None:
        return {'message': f'Связь не обнаружена с ID автора {author_id} не найдена!'}
    return result


@router.get("/get_info_by_book_id/{book_id}")
async def get_association_by_book_id(book_id: int) -> SBookAuthorAssociationGet | dict:
    result = await BookAuthorAssociationInterFace.find_one_or_none_by_id(book_id=book_id)
    if result is None:
        return {'message': f'Связь не обнаружена с ID книги {book_id} не найдена!'}
    return result