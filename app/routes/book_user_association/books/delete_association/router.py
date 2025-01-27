from fastapi import APIRouter, Depends
from app.db.models.book_user_association.interface import BookUserAssociationInterFace
from app.db.models.user.model import UserModel
from app.routes.exceptions import *
from app.routes.utils import get_current_user

router = APIRouter()

@router.delete("/delete/{book_id}")
async def delete_book_user_association(book_id: int, user_data: UserModel = Depends(get_current_user)):
    if not (user_data is None):
        check = await BookUserAssociationInterFace.delete_association_by_id(book_id=book_id, user_id=user_data.id)
        if check:
            return {"message": f"Книга с ID {book_id} больше не у пользователя!"}
        else:
            return {"message": "Ошибка при удалении связи!"}

