from fastapi import APIRouter
from .add_new_association import router_create
from .delete_association import router_delete
from .get_association_info import router_read

router = APIRouter(prefix='/book_user_association', tags=['user_association'])
router.include_router(router_create)
router.include_router(router_delete)
router.include_router(router_read)