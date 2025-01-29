from fastapi import APIRouter, Depends
from app.db.models.book.interface import BookInterFace
from app.db.models.book.model import BookModel
from app.db.models.book_user_association.interface import BookUserAssociationInterFace
from app.db.models.user.model import UserModel
from app.routes.book_user_association.add_new_association.schema import SBookUserAssociationAdd
from app.routes.exceptions import *
from app.routes.utils import get_current_user
from app.utils import get_server_book_limit

router = APIRouter()

@router.post("/add/")
async def add_new_book_user_association(new_book_user_association: SBookUserAssociationAdd, user_data: UserModel = Depends(get_current_user)) -> dict:
    if not (user_data is None):
        result = await BookUserAssociationInterFace.find_all(user_id=user_data.id)
        count_books_in_use = await BookUserAssociationInterFace.find_all(book_id=user_data.id)
        count_books:BookModel = await BookInterFace.find_one_or_none_by_id(data_id=new_book_user_association.book_id)
        print(len(result), count_books.count_copies, len(count_books_in_use))
        if count_books.count_copies > len(count_books_in_use):
            if len(result) < get_server_book_limit():
                check = await BookUserAssociationInterFace.add_new_book_user_association(**new_book_user_association.model_dump())
                if check:
                    return {"message": "Пользователь и книга связаны"}
                return {"message": "Ошибка при добавлении связи!"}
            return {"message": "Ошибка при добавлении связи! Достигнут лимит для пользователя!"}
        return {"message": "Ошибка при добавлении связи! Доступных книг нет!"}
