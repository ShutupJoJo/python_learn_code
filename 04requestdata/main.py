from fastapi import FastAPI, Path, Query, Body, Cookie, Header
from pydantic.fields import Field
from pydantic import field_validator
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()


class Item(BaseModel):
    name: str = Field(max_length=10)
    description: str | None = None
    price: float | None = 0

    @field_validator('name')
    @classmethod
    def valiate_name(cls, value: str):
        if ' ' in value:
            raise ValueError("name中不能包含空格！")
        return value


@app.get("/")
async def root():
    return {"message": "Hello World"}


# 路由上的：路径参数
@app.get("/hello/{name}")
async def say_hello(name: str = Path(max_length=10, description='这里填用户名！')):
    """
    用来给用户打招呼的路由
    :param name:
    :return:
    """
    return {"message": f"Hello {name}"}

# 路由上的：查询参数
@app.get('/books')
async def book_list(
        page: int=Query(default=1, description='页码', ge=1),
        size: int=Query(default=10, description='每页数据')
):
    return {"page": page, "size": size}


@app.put('/item/{item_id}')
async def update_item(item_id: int, item: Item=Body(description='xx')):
    print('item_id', item_id)
    print(item.name, item.description)
    return {"message": "update success"}


@app.get('/cookie/get')
async def get_cookie(username: str|None = Cookie(default=None)):
    print("username:", username)
    return "success"


@app.get('/cookie/set')
async def set_cookie():
    response = JSONResponse(content={"message": "set cookie"})
    response.set_cookie('token', 'xxx')
    return response


@app.get('/header')
async def get_header(
        user_agent: str|None=Header(default=None),
        host: str|None=Header(default=None)
):
    print('User-Agent:', user_agent)
    print('Host:', host)
    return {"message": "header"}