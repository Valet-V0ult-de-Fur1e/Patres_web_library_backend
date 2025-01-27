from fastapi import APIRouter, Depends
from app.db.models.book_author_association.interface import BookAuthorAssociationInterFace
from app.db.models.user.model import UserModel
from app.routes.book_author_association.add_new_association.schema import SBookAuthorAssociationAdd
from app.routes.exceptions import *
from app.routes.utils import get_current_user
from app.routes.exceptions import ForbiddenException

router = APIRouter()

@router.post("/add/")
async def add_new_new_book_author_association(new_book_author_association: SBookAuthorAssociationAdd, user_data: UserModel = Depends(get_current_user)) -> dict:
    if user_data.is_admin:
        check = await BookAuthorAssociationInterFace.add_new_book(**new_book_author_association.model_dump())
        if check:
            return {"message": "Автор и книга связаны"}
        else:
            return {"message": "Ошибка при добавлении связи!"}
    return ForbiddenException
