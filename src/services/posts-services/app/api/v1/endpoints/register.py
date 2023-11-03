from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class NewUser(BaseModel):
    username: str
    password: str
    name: str
    email: str


@router.post("/register")
async def register_user():
    return {"message": "Get Users"}