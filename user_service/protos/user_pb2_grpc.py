# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import user_pb2 as user__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in user_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class UserStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary(
                '/User/CreateUser',
                request_serializer=user__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=user__pb2.UserInfoResponse.FromString,
                _registered_method=True)
        self.GetUserById = channel.unary_unary(
                '/User/GetUserById',
                request_serializer=user__pb2.IdRequest.SerializeToString,
                response_deserializer=user__pb2.UserInfoResponse.FromString,
                _registered_method=True)
        self.GetUserByMobile = channel.unary_unary(
                '/User/GetUserByMobile',
                request_serializer=user__pb2.MobileRequest.SerializeToString,
                response_deserializer=user__pb2.UserInfoResponse.FromString,
                _registered_method=True)
        self.UpdateAvatar = channel.unary_unary(
                '/User/UpdateAvatar',
                request_serializer=user__pb2.AvatarRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.UpdateUsername = channel.unary_unary(
                '/User/UpdateUsername',
                request_serializer=user__pb2.UsernameRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.UpdatePassword = channel.unary_unary(
                '/User/UpdatePassword',
                request_serializer=user__pb2.PasswordRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.GetUserList = channel.unary_unary(
                '/User/GetUserList',
                request_serializer=user__pb2.PageRequest.SerializeToString,
                response_deserializer=user__pb2.UserListResponse.FromString,
                _registered_method=True)
        self.VerifyUser = channel.unary_unary(
                '/User/VerifyUser',
                request_serializer=user__pb2.VerifyUserRequest.SerializeToString,
                response_deserializer=user__pb2.UserInfoResponse.FromString,
                _registered_method=True)
        self.GetOrCreateUserByMobile = channel.unary_unary(
                '/User/GetOrCreateUserByMobile',
                request_serializer=user__pb2.MobileRequest.SerializeToString,
                response_deserializer=user__pb2.UserInfoResponse.FromString,
                _registered_method=True)


class UserServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserByMobile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAvatar(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUsername(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePassword(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerifyUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrCreateUserByMobile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=user__pb2.CreateUserRequest.FromString,
                    response_serializer=user__pb2.UserInfoResponse.SerializeToString,
            ),
            'GetUserById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserById,
                    request_deserializer=user__pb2.IdRequest.FromString,
                    response_serializer=user__pb2.UserInfoResponse.SerializeToString,
            ),
            'GetUserByMobile': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserByMobile,
                    request_deserializer=user__pb2.MobileRequest.FromString,
                    response_serializer=user__pb2.UserInfoResponse.SerializeToString,
            ),
            'UpdateAvatar': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAvatar,
                    request_deserializer=user__pb2.AvatarRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UpdateUsername': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUsername,
                    request_deserializer=user__pb2.UsernameRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UpdatePassword': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePassword,
                    request_deserializer=user__pb2.PasswordRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetUserList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserList,
                    request_deserializer=user__pb2.PageRequest.FromString,
                    response_serializer=user__pb2.UserListResponse.SerializeToString,
            ),
            'VerifyUser': grpc.unary_unary_rpc_method_handler(
                    servicer.VerifyUser,
                    request_deserializer=user__pb2.VerifyUserRequest.FromString,
                    response_serializer=user__pb2.UserInfoResponse.SerializeToString,
            ),
            'GetOrCreateUserByMobile': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrCreateUserByMobile,
                    request_deserializer=user__pb2.MobileRequest.FromString,
                    response_serializer=user__pb2.UserInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'User', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('User', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class User(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/User/CreateUser',
            user__pb2.CreateUserRequest.SerializeToString,
            user__pb2.UserInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetUserById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/User/GetUserById',
            user__pb2.IdRequest.SerializeToString,
            user__pb2.UserInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetUserByMobile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/User/GetUserByMobile',
            user__pb2.MobileRequest.SerializeToString,
            user__pb2.UserInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateAvatar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/User/UpdateAvatar',
            user__pb2.AvatarRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateUsername(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/User/UpdateUsername',
            user__pb2.UsernameRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdatePassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/User/UpdatePassword',
            user__pb2.PasswordRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetUserList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/User/GetUserList',
            user__pb2.PageRequest.SerializeToString,
            user__pb2.UserListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def VerifyUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/User/VerifyUser',
            user__pb2.VerifyUserRequest.SerializeToString,
            user__pb2.UserInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetOrCreateUserByMobile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/User/GetOrCreateUserByMobile',
            user__pb2.MobileRequest.SerializeToString,
            user__pb2.UserInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
