from fastapi import APIRouter
from .endpoints import register
from .endpoints import login

router = APIRouter()

router.include_router(register.router, prefix="/register", tags=["register"])
router.include_router(login.router, prefix="/login", tags=["register"])