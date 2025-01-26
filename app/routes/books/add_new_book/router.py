from fastapi import APIRouter, Depends
from app.db.models.book.interface import BookInterFace
from app.db.models.user.model import UserModel
from app.routes.books.add_new_book.schema import SBookAdd
from app.routes.exceptions import *
from app.routes.utils import get_current_user

router = APIRouter()

@router.post("/add/")
async def add_new_book(new_book: SBookAdd, user_data: UserModel = Depends(get_current_user)) -> dict:
    if user_data.is_admin:
        check = await BookInterFace.add_new_book(**new_book.model_dump())
        if check:
            return {"message": "Книга успешно добавлена!", "new_book": new_book}
        else:
            return {"message": "Ошибка при добавлении книги!"}
