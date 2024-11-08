from fastapi import FastAPI, Depends
from typing import Dict

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


######################函数依赖######################
async def list_common(page: int=1, size: int=10, q: str|None=None):
    # q: a+b, [a,b]
    # q: a, [a]
    query_params = []
    if q:
        query_params = q.split(" ")
    return {'page': page, 'size': size, 'query_params': query_params}

async def list_common_with_q(q: str|None=None):
    query_params = []
    if q:
        query_params = q.split(" ")
    return query_params

@app.get('/items')
async def get_items(common: Dict=Depends(list_common)):
    print('page:', common['page'])
    print('size:', common['size'])
    print('query_params:', common['query_params'])
    return {"items": ['xx', 'yy']}


@app.get('/users')
async def get_users(query_params: Dict=Depends(list_common_with_q), page: int=1, size: int=30, q: str|None=None):
    print('page:', page)
    print('size:', size)
    print('query_params:', query_params)
    return {"users": ['xx', 'yy']}
######################函数依赖######################


######################类依赖######################
class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

    def get_query_params(self):
        query_params = []
        if self.q:
            query_params = self.q.split(" ")
        return query_params

@app.get("/books")
async def get_books(params=Depends(CommonQueryParams), skip: int=0):
    print(params.q)
    print(params.get_query_params())
    print('skip:', skip)
    return {"message": "ok"}
######################类依赖######################