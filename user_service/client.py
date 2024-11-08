import grpc
from protos import user_pb2_grpc, user_pb2, address_pb2, address_pb2_grpc


def test_create_user(stub):
    try:
        request = user_pb2.CreateUserRequest()
        request.mobile = "18899990000"
        response = stub.CreateUser(request)
        # 如果直接打印response，那么只会输出那些有值的字段，没有值的字段不会输出
        # 并不代表这个字段不存在
        print(response)
    except grpc.RpcError as e:
        print(e.code())
        print(e.details())

def test_get_user_by_id(stub):
    request = user_pb2.IdRequest()
    request.id = 1820733406988730368
    response = stub.GetUserById(request)
    print(response)

def test_get_user_by_mobile(stub):
    request = user_pb2.MobileRequest()
    request.mobile = '18899990002'
    response = stub.GetUserByMobile(request)
    print(response)

def test_update_avatar(stub):
    request = user_pb2.AvatarRequest()
    request.id = 1820733406988730368
    request.avatar = 'https://www.zlkt.net/xx.jpg'
    response = stub.UpdateAvatar(request)
    print(response)

def test_update_username(stub):
    request = user_pb2.UsernameRequest()
    request.id = 1820733406988730368
    request.username = '张三'
    response = stub.UpdateUsername(request)
    print(response)

def test_update_password(stub):
    request = user_pb2.PasswordRequest()
    request.id = 1820733406988730368
    request.password = '111111'
    response = stub.UpdatePassword(request)
    print(response)


def test_verify_user(stub):
    request = user_pb2.VerifyUserRequest()
    request.mobile = '18899990000'
    request.password = '111112'
    response = stub.VerifyUser(request)
    print(response)

def test_get_user_list(stub):
    request = user_pb2.PageRequest()
    request.page = 2
    request.size = 1
    response = stub.GetUserList(request)
    print(response)

def test_get_or_create_user(stub):
    request = user_pb2.MobileRequest()
    request.mobile = '18899990002'
    response = stub.GetOrCreateUserByMobile(request)
    print(response)

def test_create_address(stub):
    request = address_pb2.CreateAddressRequest(
        user_id=1823301044390592512,
        realname='孙悟空',
        mobile='18899991111',
        region='北京市朝阳区',
        detail='白家庄东里',
    )
    response = stub.CreateAddress(request)
    print(response.address)

def test_update_address(stub):
    request = address_pb2.UpdateAddressRequest(
        id="0be2002f956449aba70d3a5baac56451",
        realname="猪八戒",
        mobile='19900001111',
        region='北京市朝阳区',
        detail='白家庄东里',
        user_id=1823301044390592512
    )
    stub.UpdateAddress(request)

def test_delete_address(stub):
    request = address_pb2.DeleteAddressRequest(
        user_id=1823301044390592512,
        id="0be2002f956449aba70d3a5baac56451"
    )
    stub.DeleteAddress(request)

def test_get_address_by_id(stub):
    request = address_pb2.AddressIdRequest(
        id="8ff0721081df407bb3682f724bf916c2",
        user_id=1823301044390592512
    )
    address = stub.GetAddressById(request)
    print(address)

def test_get_address_list(stub):
    request = address_pb2.AddressListRequest(
        user_id=1823301044390592512,
        page=1,
        size=10
    )
    addresses = stub.GetAddressList(request)
    print(addresses)

def main():
    with grpc.insecure_channel("127.0.0.1:5001") as channel:
        # stub = user_pb2_grpc.UserStub(channel)
        # test_create_user(stub)
        # test_get_user_by_id(stub)
        # test_get_user_by_mobile(stub)
        # test_update_avatar(stub)
        # test_update_username(stub)
        # test_update_password(stub)
        # test_verify_user(stub)
        # test_get_user_list(stub)
        # test_get_or_create_user(stub)

        address_stub = address_pb2_grpc.AddressStub(channel)
        # test_create_address(address_stub)
        # test_update_address(address_stub)
        # test_delete_address(address_stub)
        # test_get_address_by_id(address_stub)
        test_get_address_list(address_stub)


if __name__ == '__main__':
    main()