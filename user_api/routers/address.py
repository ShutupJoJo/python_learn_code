from fastapi import APIRouter, HTTPException
from schemas.response import AddressModel, ResultModel, AddressListModel
from schemas.request import CreateAddressModel, DeleteAddressModel, UpdateAddressModel
from utils.auth import AuthHandler
from services.address import AddressServiceClient
from fastapi import status
from fastapi import Depends

router = APIRouter(prefix='/address')

auth_handler = AuthHandler()
address_service_client = AddressServiceClient()


@router.post('/create', response_model=AddressModel)
async def create_address(data: CreateAddressModel, user_id: int=Depends(auth_handler.auth_access_dependency)):
    address = await address_service_client.create_address(
        user_id,
        realname=data.realname,
        mobile=data.mobile,
        region=data.region,
        detail=data.detail
    )
    return address


@router.delete('/delete', response_model=ResultModel)
async def delete_address(data: DeleteAddressModel, user_id: int=Depends(auth_handler.auth_access_dependency)):
    await address_service_client.delete_address(user_id, data.id)
    return ResultModel()


@router.put('/update', response_model=ResultModel)
async def update_address(data: UpdateAddressModel, user_id: int=Depends(auth_handler.auth_access_dependency)):
    await address_service_client.update_address(
        id=data.id,
        realname=data.realname,
        mobile=data.mobile,
        region=data.region,
        detail=data.detail,
        user_id=user_id,
    )
    return ResultModel()

@router.get('/detail/{id}', response_model=AddressModel)
async def update_address(id: str, user_id: int=Depends(auth_handler.auth_access_dependency)):
    address = await address_service_client.get_address_by_id(user_id, id)
    return address

# /address/list?page=1&size=20
@router.get('/list', response_model=AddressListModel)
async def update_address(page: int=1, size: int=10, user_id: int=Depends(auth_handler.auth_access_dependency)):
    addresses = await address_service_client.get_address_list(user_id, page=page, size=size)
    return {"addresses": addresses}
