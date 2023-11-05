from fastapi import FastAPI
from mangum import Mangum

from app.api.v1.api import router as api_v1_router

root_path = "/auth-api"

app = FastAPI(root_path=root_path)


@app.get(root_path)
async def root():
    return {"message": "Hello from Auth Services"}

app.include_router(api_v1_router, prefix="/v1")
handler = Mangum(app)