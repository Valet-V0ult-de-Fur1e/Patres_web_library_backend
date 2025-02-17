from fastapi import APIRouter, Depends
from app.db.models.book_user_association.interface import BookUserAssociationInterFace
from app.db.models.user.model import UserModel
from app.routes.exceptions import *
from app.routes.utils import get_current_user

router = APIRouter()


@router.get("/get_info_by_user_id")
async def get_association_by_user_id(user_data: UserModel = Depends(get_current_user)):
    result = await BookUserAssociationInterFace.find_all(user_id=user_data.id)
    if result is None:
        return {'message': f'Связь не обнаружена с ID {user_data.id} !'}
    return result