import os

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UpdateRequest(BaseModel):
    id: int
    name: str
    description: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/thing")
async def thing():
    return {"thing": "here is the thing you were looking for"}


@app.get("/env")
async def env():
    return {"env": os.environ.get("NICE_ENV")}


@app.get("/cron")
async def cron():
    print("cron job")
    return {"message": "success"}


@app.post("/update")
async def update(req: UpdateRequest):
    print(req)
    return {"message": "update successful"}
