from protos import user_pb2
from protos import user_pb2_grpc
import grpc


def create_user(stub):
    try:
        request = user_pb2.CreateUserRequest()
        request.mobile = "18899990000"
        response = stub.CreateUser(request)
        print(response.user.mobile)
    except grpc.RpcError as e:
        print(e.code())
        print(e.details())


def get_user_by_id(stub):
    request = user_pb2.IdRequest()
    request.id = 1820372832928923648
    response = stub.GetUserById(request)
    print(response.user.mobile)

def get_user_by_mobile(stub):
    request = user_pb2.MobileRequest()
    request.mobile = '18899990000'
    response = stub.GetUserByMobile(request)
    print(response.user.mobile)

def update_username(stub):
    request = user_pb2.UpdateUsernameRequest()
    request.id = 1820372832928923648
    request.username = '张三'
    response = stub.UpdateUsername(request)
    print(response)

def update_password(stub):
    request = user_pb2.UpdatePasswordRequest()
    request.id = 1820372832928923648
    request.password = '123456'
    response = stub.UpdatePassword(request)
    print(response)

def get_user_list(stub):
    request = user_pb2.PageRequest()
    request.page = 1
    request.size = 10
    response = stub.GetUserList(request)
    print(response)

def verify_user(stub):
    request = user_pb2.VerifyUserRequest()
    request.mobile = '18899990000'
    request.password = "123456"
    response = stub.VerifyUser(request)
    print(response)

def main():
    with grpc.insecure_channel("127.0.0.1:5001") as channel:
        stub = user_pb2_grpc.UserStub(channel)
        # create_user(stub)
        # get_user_by_id(stub)
        # get_user_by_mobile(stub)
        # update_username(stub)
        # update_password(stub)
        # get_user_list(stub)
        verify_user(stub)




if __name__ == '__main__':
    main()