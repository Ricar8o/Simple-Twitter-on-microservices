from fastapi import FastAPI
from mangum import Mangum

from app.api.v1.api import router as api_v1_router


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from Auth Services"}

app.include_router(api_v1_router, prefix="/api/v1")
handler = Mangum(app)