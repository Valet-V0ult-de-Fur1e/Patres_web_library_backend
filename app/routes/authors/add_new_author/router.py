from fastapi import APIRouter, Depends
from app.routes.authors.add_new_author.schema import SAuthorAdd
from app.db.models.user.model import UserModel
from app.db.models.author.interface import AuthorInterFace
from app.routes.exceptions import *
from app.routes.utils import get_current_user
from app.routes.exceptions import ForbiddenException
router = APIRouter()

@router.post("/add/")
async def add_new_author(new_author: SAuthorAdd, user_data: UserModel = Depends(get_current_user)) -> dict:
    if user_data.is_admin:
        check = await AuthorInterFace.add_new_author(**new_author.model_dump())
        if check:
            return {"message": "Автор успешно добавлен!", "new_author": new_author}
        else:
            return {"message": "Ошибка при добавлении автора!"}
    return ForbiddenException