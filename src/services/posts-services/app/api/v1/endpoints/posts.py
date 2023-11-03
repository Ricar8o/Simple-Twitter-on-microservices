from fastapi import APIRouter
from pydantic import BaseModel
from .data import users, posts, lastId

router = APIRouter()

class PostDto(BaseModel):
    content: str
    authorId: int

class UpdatePostDto(BaseModel):
    content: str

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

@router.get("{postId}")
async def get_post_by_id(postId: int):
    for post in posts:
        if post["id"] == postId:
            return post

@router.put("{postId}")
async def update_post(postId: int, update_post: UpdatePostDto):
    post_index = None
    saved_post = None
    for index in range(len(posts)):
        post = posts[index]
        if post["id"] == postId:
            post_index = index
            saved_post = posts[post_index]
            break
    if not post_index:
        return {"error": "Post not found"}

    newPost = {
        "id": postId,
        "content": update_post.content,
        "author": saved_post["author"],
        "comments": saved_post["comments"]
    }
    posts[post_index] = newPost
    return newPost

@router.delete("{postId}")
async def delete_post(postId: int):
    post_index = None
    for index in range(len(posts)):
        post = posts[index]
        if post["id"] == postId:
            post_index = index
            break
    if not post_index:
        return {"error": "Post not found"}

    posts.pop(post_index)