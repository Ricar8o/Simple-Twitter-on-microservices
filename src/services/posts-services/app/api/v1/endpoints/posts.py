from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .data import users, posts, lastId

router = APIRouter()

class PostDto(BaseModel):
    content: str
    authorId: int

class UpdatePostDto(BaseModel):
    content: str


def search_post_index(postId: int):
    for index in range(len(posts)):
        post = posts[index]
        if post["id"] == postId:
            return index
    return None

@router.post("")
async def create_post(post: PostDto):
    global lastId
    if post.authorId > len(users) or post.authorId <= 0:
        return {"error": "User not found"}
    posts.append(
        {
            "id": lastId,
            "content": post.content,
            "author": users[post.authorId - 1],
            "comments": []
        }
    )
    lastId += 1
    return posts

@router.get("/{postId}")
async def get_post_by_id(postId: int):
    for post in posts:
        if post["id"] == postId:
            return post

@router.put("/{postId}")
async def update_post(postId: int, update_post: UpdatePostDto):
    post_index = search_post_index(postId)

    if post_index is None:
        raise HTTPException(status_code=404, detail="Post not found")

    saved_post = posts[post_index]

    newPost = {
        "id": postId,
        "content": update_post.content,
        "author": saved_post["author"],
        "comments": saved_post["comments"]
    }
    posts[post_index] = newPost
    return newPost

@router.delete("/{postId}")
async def delete_post(postId: int):
    post_index = search_post_index(postId)

    if post_index is None:
        raise HTTPException(status_code=404, detail="Post not found")

    posts.pop(post_index)
    return {"message": "Post deleted"}

@router.post("/{postId}/comments", tags=["comments"])
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

@router.get("/{postId}/comments", tags=["comments"])
async def get_comments(postId: int):
    post_index = search_post_index(postId)

    if post_index is None:
        raise HTTPException(status_code=404, detail="Post not found")

    return posts[post_index]["comments"]