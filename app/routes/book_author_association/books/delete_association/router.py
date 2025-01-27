from fastapi import APIRouter, Depends
from app.db.models.book_author_association.interface import BookAuthorAssociationInterFace
from app.db.models.user.model import UserModel
from app.routes.exceptions import *
from app.routes.utils import get_current_user

router = APIRouter()

@router.delete("/delete/{book_id}/{author_id}")
async def delete_book_author_association(book_id: int, author_id: int, user_data: UserModel = Depends(get_current_user)):
    if user_data.is_admin:
        check = await BookAuthorAssociationInterFace.delete_association_by_id(book_id=book_id, author_id=author_id)
        if check:
            return {"message": f"Автор с ID больше не создатель книги с ID {book_id} удалена!"}
        else:
            return {"message": "Ошибка при удалении связи!"}

