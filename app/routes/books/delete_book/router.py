from fastapi import APIRouter, Depends
from app.db.models.book.interface import BookInterFace
from app.db.models.book_author_association.interface import BookAuthorAssociationInterFace
from app.db.models.user.model import UserModel
from app.routes.exceptions import *
from app.routes.utils import get_current_user
from app.routes.exceptions import ForbiddenException
router = APIRouter()

@router.delete("/delete/{book_id}")
async def delete_author(book_id: int, user_data: UserModel = Depends(get_current_user)):
    if user_data.is_admin:
        await BookAuthorAssociationInterFace.delete_association_by_book_id(book_id=book_id)
        check = await BookInterFace.delete_book_by_id(id=book_id)
        if check:
            return {"message": f"Книга с ID {book_id} удалена!"}
        else:
            return {"message": "Ошибка при удалении книги!"}
    return ForbiddenException
