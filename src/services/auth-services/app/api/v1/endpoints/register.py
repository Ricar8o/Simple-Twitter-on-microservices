from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class NewUser(BaseModel):
    username: str
    password: str
    name: str
    email: str


@router.post("")
async def register_user(new_user: NewUser):
    return {"message": f"New User {new_user.username} registered successfully"}