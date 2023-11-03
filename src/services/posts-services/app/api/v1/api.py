from fastapi import APIRouter
from .endpoints import feed

router = APIRouter()

router.include_router(feed.router, prefix="/feed", tags=["feed", "posts"])