from fastapi import APIRouter, Depends
from app.db.models.user.interface import UserInterFace
from app.db.models.user.model import UserModel
from app.routes.exceptions import *
from app.routes.users.update.schema import SUserUpdate
from app.routes.utils import get_current_user
from app.routes.exceptions import ForbiddenException

router = APIRouter()

@router.put("/update")
async def update_user(new_user_data: SUserUpdate, user_data: UserModel = Depends(get_current_user)) -> dict:
    check = await UserInterFace.update(filter_by={'id': user_data.id},
                                email=new_user_data.email,
                                first_name=new_user_data.first_name,
                                last_name=new_user_data.last_name,
                                password=new_user_data.password
                                )
    if check:
        return {"message": "Данные пользователя успешно обновлены!", "user": new_user_data}
    else:
        return {"message": "Ошибка при обновлении данных книги!"}


@router.put("/update_user_status/{user_id}")
async def update_user(user_id: int, user_data: UserModel = Depends(get_current_user)) -> dict:
    if user_data.is_admin:
        current_user_data:UserModel = await UserInterFace.find_one_or_none_by_id(user_id)
        check = await UserInterFace.update(filter_by={'id': user_data.id},
                                    is_admin=(not bool(current_user_data.is_admin))
                                    )
        if check:
            return {"message": "Данные пользователя успешно обновлены!"}
        else:
            return {"message": "Ошибка при обновлении данных книги!"}
    return ForbiddenException

