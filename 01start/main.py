from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get('/')
async def index():
    return {"message": "Hello FastXXX"}


@app.get('/item/{item_id}')
async def item(item_id: int, q: Optional[str]=None):
    return {"item_id": item_id, "q": q}