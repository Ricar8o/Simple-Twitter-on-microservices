from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

users = [
    {
        "id": 1,
        "username": "johndoe",
        "name": "John Doe",
        "email": "john.doe@mail.example.com"
    },
    {
        "id": 2,
        "username": "janedoe",
        "name": "Jane Doe",
        "email": "jane.doe@mail.example.com"
    },
    {
        "id": 3,
        "username": "pparker",
        "name": "Peter Parker",
        "email": "peter.parker@spider.mail.com"
    },
    {
        "id": 4,
        "username": "gstacy",
        "name": "Gwen Stacy",
        "email": "gwen.stacy@spider.mail.com"
    }
]

posts = [
    {
        "id": 1,
        "content": "Hello world",
        "author": users[0],
        "comments": []
    },
    {
        "id": 2,
        "content": "Lorem ipsum dolor sit amet",
        "author": users[1],
        "comments": [
            {
                "id": 1,
                "content": "Great post!",
                "author": users[0]
            }
        ],
    },
    {
        "id": 3,
        "content": "With great power, comes great responsibility",
        "author": users[2],
        "comments": []
    },
    {
        "id": 4,
        "content": "I'm Spider-Woman. I'm strong and I'm not afraid.",
        "author": users[3],
        "comments": [
            {
                "id": 2,
                "content": "You're doing great, Gwen!",
                "author": users[2]
            }
        ],
    },
]

lastId = 5

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