from fastapi import APIRouter
from .endpoints import feed, posts, comments, likes

router = APIRouter()

router.include_router(feed.router, prefix="/feed", tags=["Feed"])
router.include_router(posts.router, prefix="/posts", tags=["Posts"])
router.include_router(comments.router, prefix="/posts/{postId}/comments", tags=["Comments"])
router.include_router(likes.router, prefix="/posts/{postId}/likes", tags=["Likes"])