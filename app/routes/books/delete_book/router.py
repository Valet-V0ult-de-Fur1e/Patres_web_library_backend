from fastapi import APIRouter, Depends
from app.db.models.book.interface import BookInterFace
from app.db.models.user.model import UserModel
from app.routes.exceptions import *
from app.routes.utils import get_current_user

router = APIRouter()

@router.delete("/delete/{book_id}")
async def delete_author(book_id: int, user_data: UserModel = Depends(get_current_user)):
    if user_data.is_admin:
        check = await BookInterFace.delete_book_by_id(id=book_id)
        if check:
            return {"message": f"Книга с ID {book_id} удалена!"}
        else:
            return {"message": "Ошибка при удалении книги!"}

