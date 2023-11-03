from fastapi import APIRouter

router = APIRouter()

feed = [
    {
        "id": 1,
        "content": "Hello world",
        "author": {
            "id": 1,
            "username": "johndoe",
            "name": "John Doe",
            "email": "john.doe@mail.example.com"
        }
    },
    {
        "id": 2,
        "content": "Lorem ipsum dolor sit amet",
        "author": {
            "id": 2,
            "username": "janedoe",
            "name": "Jane Doe",
            "email": "jane.doe@mail.example.com"
        },
        "comments": [
            {
                "id": 1,
                "content": "Great post!",
                "author": {
                    "id": 3,
                    "username": "johndoe",
                    "name": "John Doe",
                    "email": "john.doe@mail.example.com"
                }
            }
        ],
    },
    {
        "id": 3,
        "content": "With great power, comes great responsibility",
        "author": {
            "id": 3,
            "username": "pparker",
            "name": "Peter Parker",
            "email": "peter.parker@spider.mail.com"
        }
    },
    {
        "id": 4,
        "content": "I'm Spider-Woman. I'm strong and I'm not afraid.",
        "author": {
            "id": 4,
            "username": "gstacy",
            "name": "Gwen Stacy",
            "email": "gwen.stacy@spider.mail.com"
        },
        "comments": [
            {
                "id": 2,
                "content": "You're doing great, Gwen!",
                "author": {
                    "id": 3,
                    "username": "pparker",
                    "name": "Peter Parker",
                    "email": "peter.parker@spider.mail.com"
                }
            }
        ],
    },

]


@router.get("")
async def get_feed():
    return feed