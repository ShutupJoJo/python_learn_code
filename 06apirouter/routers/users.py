from fastapi import APIRouter

router = APIRouter(prefix='/user', tags=['用户'])


@router.get('/list')
async def get_user_list():
    return [
        {'username': "zhangsan", 'email': "zhangsan@qq.com"}
    ]