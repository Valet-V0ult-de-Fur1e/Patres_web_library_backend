from fastapi import APIRouter, Depends
from app.db.models.author.interface import AuthorInterFace
from app.db.models.user.model import UserModel
from app.routes.authors.update_author_info.schema import SAuthorUpdate
from app.routes.exceptions import *
from app.routes.utils import get_current_user

router = APIRouter()

@router.put("/update")
async def update_author(author_new_data: SAuthorUpdate, user_data: UserModel = Depends(get_current_user)) -> dict:
    if user_data.is_admin:
        check = await AuthorInterFace.update(filter_by={'id': author_new_data.id},
                                   first_name=author_new_data.first_name,
                                   last_name=author_new_data.last_name,
                                   biography=author_new_data.biography,
                                   birth_date=author_new_data.birth_date)
        if check:
            return {"message": "Данные автора успешно обновлены!", "author": author_new_data}
        else:
            return {"message": "Ошибка при обновлении данных автора!"}

