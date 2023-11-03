from fastapi import APIRouter, HTTPException
from .data import users, posts
from .posts import PostDto, search_post_index

router = APIRouter()

@router.post("")
async def comment_post(postId: int, comment: PostDto):
    post_index = search_post_index(postId)

    if post_index is None:
        raise HTTPException(status_code=404, detail="Post not found")
    if comment.authorId > len(users) or comment.authorId <= 0:
        return {"error": "User not found"}

    posts[post_index]["comments"].append(
        {
            "content": comment.content,
            "author": users[comment.authorId - 1],
        }
    )

    return posts

@router.get("")
async def get_comments(postId: int):
    post_index = search_post_index(postId)

    if post_index is None:
        raise HTTPException(status_code=404, detail="Post not found")

    return posts[post_index]["comments"]