from fastapi import APIRouter, Depends
from app.db.models.book.interface import BookInterFace
from app.db.models.user.model import UserModel
from app.routes.books.update_book_info.schema import SBookUpdate
from app.routes.exceptions import *
from app.routes.utils import get_current_user

router = APIRouter()

@router.put("/update")
async def update_book(book_new_data: SBookUpdate, user_data: UserModel = Depends(get_current_user)) -> dict:
    if user_data.is_admin:
        check = await BookInterFace.update(filter_by={'id': book_new_data.id},
                                   title=book_new_data.title,
                                   publication_date=book_new_data.publication_date,
                                   count_copies=book_new_data.count_copies,
                                   )
        if check:
            return {"message": "Данные книги успешно обновлены!", "book": book_new_data}
        else:
            return {"message": "Ошибка при обновлении данных книги!"}

