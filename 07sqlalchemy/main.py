from fastapi import FastAPI
from routers import users
from middlewares import dbs
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

# 添加路由
app.include_router(users.router)

# 添加中间件
app.add_middleware(BaseHTTPMiddleware, dispatch=dbs.create_session_middleware)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
