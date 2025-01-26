from fastapi import APIRouter
from .add_new_book import router_create
from .delete_book import router_delete
from .get_book_info import router_read
from .update_book_info import router_update

router = APIRouter(prefix='/books', tags=['Books'])
router.include_router(router_create)
router.include_router(router_delete)
router.include_router(router_read)
router.include_router(router_update)