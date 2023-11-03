from fastapi import APIRouter, HTTPException


router = APIRouter()

users = [
    {
        "id": 1,
        "username": "johndoe",
        "name": "John Doe",
        "email": "john.doe@mail.example.com",
        "posts": [
            {
                "id": 1,
                "content": "What´s up, guys?",
            }
        ]
    },
    {
        "id": 2,
        "username": "janedoe",
        "name": "Jane Doe",
        "email": "jane.doe@mail.example.com",
        "posts": [
            {
                "id": 2,
                "content": "Hello, world! I'm Jane Doe!",
            }
        ]
    },
    {
        "id": 3,
        "username": "pparker",
        "name": "Peter Parker",
        "email": "peter.parker@spider.mail.com",
        "posts": [
            {
                "id": 3,
                "content": "With great power comes great responsibility.",
            },
            {
                "id": 4,
                "content": "My spider-sense is tingling.",
            },
            {
                "id": 5,
                "content": "Someday, I'll be living in a big old city.",
            }
        ]
    },
    {
        "id": 4,
        "username": "gstacy",
        "name": "Gwen Stacy",
        "email": "gwen.stacy@spider.mail.com",
        "posts": [
            {
                "id": 6,
                "content": "I'm following Peter Parker.",
            },
            {
                "id": 7,
                "content": "I'm following Mary Jane.",
            },
            {
                "id": 8,
                "content": "I'm following Harry Osborn.",
            },
            {
                "id": 9,
                "content": "I'm listening Mr Brightside. from The Killers, it's a great song!",
            }
        ]
    }
]


def search_user_index(user_id: int):
    for index in range(len(users)):
        user = users[index]
        if user["id"] == user_id:
            return index
    return None


@router.post("/{user_id}/follow")
async def follow_user(user_id: int):
    user_index = search_user_index(user_id)
    if user_index is None:
        raise HTTPException(status_code=404, detail="User not found")
    user = users[user_index]

    return {"message": f"You are now following {user['username']}"}

@router.post("/{user_id}/unfollow")
async def unfollow_user(user_id: int):
    user_index = search_user_index(user_id)
    if user_index is None:
        raise HTTPException(status_code=404, detail="User not found")
    user = users[user_index]

    return {"message": f"You are no longer following {user['username']}"}

@router.get("/{user_id}/followers")
async def get_user_followers(user_id: int):
    user_index = search_user_index(user_id)
    if user_index is None:
        raise HTTPException(status_code=404, detail="User not found")
    user = users[user_index]

    return {"message": f"Followers of {user['username']}"}

@router.post("/{user_id}/following")
async def get_user_following(user_id: int):
    user_index = search_user_index(user_id)
    if user_index is None:
        raise HTTPException(status_code=404, detail="User not found")
    user = users[user_index]

    return {"message": f"{user['username']} is following users"}

@router.post("/{user_id}/posts")
async def get_user_posts(user_id: int):
    user_index = search_user_index(user_id)
    if user_index is None:
        raise HTTPException(status_code=404, detail="User not found")
    user = users[user_index]

    return user['posts']