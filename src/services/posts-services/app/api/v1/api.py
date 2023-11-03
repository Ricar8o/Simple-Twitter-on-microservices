from fastapi import APIRouter
from .endpoints import feed, posts

router = APIRouter()

router.include_router(feed.router, prefix="/feed", tags=["feed", "posts"])
router.include_router(posts.router, prefix="/posts", tags=["posts"])