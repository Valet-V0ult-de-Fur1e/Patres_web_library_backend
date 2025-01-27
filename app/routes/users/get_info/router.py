from fastapi import APIRouter, Depends
from app.db.models.user.interface import UserInterFace
from app.db.models.user.model import UserModel
from app.routes.utils import get_current_user
from app.routes.exceptions import ForbiddenException

router = APIRouter()

@router.get("/get_users_list")
async def get_users_list(user_data: UserModel = Depends(get_current_user)):
    if user_data.is_admin:
        return await UserInterFace.find_all()
    else:
        return ForbiddenException