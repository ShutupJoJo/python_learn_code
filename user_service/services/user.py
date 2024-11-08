import sqlalchemy.exc

from protos import user_pb2, user_pb2_grpc
from models.user import User
import grpc
from sqlalchemy import select, update
from google.protobuf import empty_pb2
from utils import pwdutil
from loguru import logger


class UserServicer(user_pb2_grpc.UserServicer):
    async def CreateUser(self, request: user_pb2.CreateUserRequest, context, session):
        mobile = request.mobile
        try:
            async with session.begin():
                user = User(mobile=mobile)
                session.add(user)
                # sqlalchemy_serializer
            response = user_pb2.UserInfoResponse(user=user.to_dict())
            return response
        except sqlalchemy.exc.IntegrityError:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details('该手机号已经存在！')

    async def GetUserById(self, request: user_pb2.IdRequest, context, session):
        try:
            async with session.begin():
                user_id = request.id
                query = await session.execute(select(User).where(User.id==user_id))
                user = query.scalar()
                if not user:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    context.set_details('该用户不存在！')
                else:
                    response = user_pb2.UserInfoResponse(user=user.to_dict())
                    return response
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('服务器错误！')

    async def GetUserByMobile(self, request: user_pb2.MobileRequest, context, session):
        try:
            async with session.begin():
                mobile = request.mobile
                query = await session.execute(select(User).where(User.mobile==mobile))
                user = query.scalar()
                if not user:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    context.set_details('该用户不存在！')
                else:
                    response = user_pb2.UserInfoResponse(user=user.to_dict())
                    return response
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('服务器错误！')

    async def UpdateAvatar(self, request: user_pb2.AvatarRequest, context, session):
        async with session.begin():
            user_id = request.id
            avatar = request.avatar
            stmt = update(User).where(User.id == user_id).values(avatar=avatar)
            result = await session.execute(stmt)
            # async sqlalchemy
            rowcount = result.rowcount
            if rowcount == 0:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details(f'ID{user_id}不存在！')
            else:
                return empty_pb2.Empty()

    async def UpdateUsername(self, request: user_pb2.AvatarRequest, context, session):
        async with session.begin():
            user_id = request.id
            username = request.username
            stmt = update(User).where(User.id == user_id).values(username=username)
            result = await session.execute(stmt)
            # async sqlalchemy
            rowcount = result.rowcount
            if rowcount == 0:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details(f'ID{user_id}不存在！')
            else:
                return empty_pb2.Empty()

    async def UpdatePassword(self, request: user_pb2.PasswordRequest, context, session):
        async with session.begin():
            user_id = request.id
            password = request.password
            hashed_password = pwdutil.hash_password(password)
            stmt = update(User).where(User.id == user_id).values(password=hashed_password)
            result = await session.execute(stmt)
            # async sqlalchemy
            rowcount = result.rowcount
            if rowcount == 0:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details(f'ID{user_id}不存在！')
            else:
                return empty_pb2.Empty()

    async def VerifyUser(self, request: user_pb2.VerifyUserRequest, context, session):
        async with session.begin():
            mobile = request.mobile
            password = request.password
            result = await session.execute(select(User).where(User.mobile==mobile))
            user = result.scalar()
            if not user:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details('该用户不存在！')
            if not pwdutil.check_password(password, user.password):
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details('密码错误！')
            reponse = user_pb2.UserInfoResponse(user=user.to_dict())
            return reponse

    async def GetUserList(self, request: user_pb2.PageRequest, context, session):
        async with session.begin():
            page = request.page
            size = request.size
            # limit/offset
            offset = (page-1)*size
            query = await session.execute(select(User).limit(size).offset(offset))
            # [(User1, ), (User2, ), ...]
            # [User1, User2, User3, ...]
            result = query.scalars().fetchall()
            # 转换为字典
            users = []
            for user in result:
                users.append(user.to_dict())
            response = user_pb2.UserListResponse(users=users)
            return response

    async def GetOrCreateUserByMobile(self, request: user_pb2.MobileRequest, context, session):
        async with session.begin():
            mobile = request.mobile
            query = await session.execute(select(User).where(User.mobile == mobile))
            user = query.scalar()
            if not user:
                user = User(mobile=mobile)
                session.add(user)
        response = user_pb2.UserInfoResponse(user=user.to_dict())
        logger.info('收到！')
        return response