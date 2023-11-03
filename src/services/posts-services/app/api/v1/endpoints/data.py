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
