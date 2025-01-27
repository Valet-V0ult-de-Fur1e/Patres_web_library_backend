from fastapi import APIRouter, Depends
from app.db.models.book_user_association.interface import BookUserAssociationInterFace
from app.db.models.user.model import UserModel
from app.routes.book_user_association.books.add_new_association.schema import SBookUserAssociationAdd
from app.routes.exceptions import *
from app.routes.utils import get_current_user
from app.utils import get_server_book_limit

router = APIRouter()

@router.post("/add/")
async def add_new_new_book_user_association(new_book_user_association: SBookUserAssociationAdd, user_data: UserModel = Depends(get_current_user)) -> dict:
    if not (user_data is None):
        result = await BookUserAssociationInterFace.find_all(user_id=user_data.id)
        check = await BookUserAssociationInterFace.add_new_book(**new_book_user_association.model_dump())
        if check and len(result) < get_server_book_limit():
            return {"message": "Пользователь и книга связаны"}
        else:
            return {"message": "Ошибка при добавлении связи!"}
