from fastapi import APIRouter
from .get_info import router as router_get_info
from .update import router as router_update

router = APIRouter(prefix='/users', tags=['Admin'])

router.include_router(router_get_info)
router.include_router(router_update)