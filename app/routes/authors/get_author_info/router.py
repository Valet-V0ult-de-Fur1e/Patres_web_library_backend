from fastapi import APIRouter, Depends
from app.db.models.author.interface import AuthorInterFace
from app.routes.authors.get_author_info.rb import RBAuthor
from app.routes.authors.get_author_info.schema import SAuthorGet
from app.routes.exceptions import *

router = APIRouter()

@router.get("/get_all")
async def get_all_authors(request_body: RBAuthor = Depends()) -> list[SAuthorGet]:
    return await AuthorInterFace.find_all(**request_body.to_dict())


@router.get("/get_info/{author_id}")
async def get_author_by_id(author_id: int) -> SAuthorGet | dict:
    result = await AuthorInterFace.find_one_or_none_by_id(id=author_id)
    if result is None:
        return {'message': f'Автор с ID {author_id} не найден!'}
    return result


@router.get("/get_by_filter")
async def get_author_by_filter(request_body: RBAuthor = Depends()) -> RBAuthor | dict:
    result = await AuthorInterFace.find_one_or_none(**request_body.to_dict())
    if result is None:
        return {'message': f'Автор с указанными параметрами не найден!'}
    return result
  