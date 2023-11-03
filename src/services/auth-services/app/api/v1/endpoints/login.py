from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class LoginParams(BaseModel):
    username: str
    password: str


@router.post("")
async def login(login_params: LoginParams):
    return {"message": "User logged in successfully"}