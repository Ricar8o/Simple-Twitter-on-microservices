from fastapi import APIRouter, HTTPException
from .posts import search_post_index

router = APIRouter()

@router.post("")
async def like_post(postId: int):
    post_index = search_post_index(postId)
    if post_index is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post liked"}

@router.delete("")
async def remove_like(postId: int):
    post_index = search_post_index(postId)
    if post_index is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Like removed"}
