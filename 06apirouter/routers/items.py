from fastapi import APIRouter, Header, Depends
from fastapi.exceptions import HTTPException

async def login_required(token: str=Header()):
    if token != "xx":
        raise HTTPException(status_code=400, detail="Token验证失败！")


router = APIRouter(prefix='/item', tags=['item'], dependencies=[Depends(login_required)])


@router.get('/list')
async def item_list():
    return {"items": [{
        'title': "xxxxxx"
    }]}
