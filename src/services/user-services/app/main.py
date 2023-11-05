from fastapi import FastAPI
from mangum import Mangum

from app.api.v1.api import router as api_v1_router

root_path = "/users-api"

app = FastAPI()


@app.get(root_path)
async def root():
    return {"message": "Hello from User Services"}

app.include_router(api_v1_router, prefix=root_path + "/v1")
handler = Mangum(app)