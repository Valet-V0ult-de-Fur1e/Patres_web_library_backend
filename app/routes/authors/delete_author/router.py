from fastapi import APIRouter, Depends
from app.db.models.author.interface import AuthorInterFace
from app.db.models.book_author_association.interface import BookAuthorAssociationInterFace
from app.db.models.user.model import UserModel
from app.routes.exceptions import *
from app.routes.utils import get_current_user

router = APIRouter()

@router.delete("/delete/{author_id}")
async def delete_author(author_id: int, user_data: UserModel = Depends(get_current_user)):
    if user_data.is_admin:
        await BookAuthorAssociationInterFace.delete_association_by_author_id(author_id=author_id)
        check = await AuthorInterFace.delete_author_by_id(id=author_id)
        if check:
            return {"message": f"Автор с ID {author_id} удален!"}
        else:
            return {"message": "Ошибка при удалении автора!"}      