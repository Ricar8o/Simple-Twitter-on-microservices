from fastapi import FastAPI
from mangum import Mangum

from app.api.v1.api import router as api_v1_router


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from Posts Services"}

app.include_router(api_v1_router, prefix="/v1")
handler = Mangum(app)