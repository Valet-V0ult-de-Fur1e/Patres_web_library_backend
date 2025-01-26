from fastapi import APIRouter
from .add_new_author import router_create
from .delete_author import router_delete
from .get_author_info import router_read
from .update_author_info import router_update

router = APIRouter(prefix='/authors', tags=['Authors'])
router.include_router(router_create)
router.include_router(router_delete)
router.include_router(router_read)
router.include_router(router_update)