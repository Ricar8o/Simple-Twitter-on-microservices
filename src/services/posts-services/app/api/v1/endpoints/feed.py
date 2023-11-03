from fastapi import APIRouter
from .data import posts

router = APIRouter()

@router.get("")
async def get_feed():
    return posts