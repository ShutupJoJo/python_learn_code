from adrf.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .authentications import AsyncAuthentication
from .permissions import AsyncPermission
from rest_framework import permissions
from .throttles import AsyncThrottle
from rest_framework import throttling
from adrf.viewsets import ViewSet
from django.contrib.auth import get_user_model
from .serializers import AsyncLoginSerializer, UserSerializer
from django.contrib.auth import aauthenticate



User = get_user_model()


class IndexView(APIView):
    async def get(self, request):
        print(request.user)
        return JsonResponse({"message": "请求正常！"})


class MessageView(APIView):
    authentication_classes = [AsyncAuthentication]
    async def post(self, request):
        title = request.data.get('title')
        content = request.data.get('content')
        print(title, content)
        return JsonResponse({"message": "您的建议已收到！"})


class UserInfoView(APIView):
    # permission_classes = [AsyncPermission]
    throttle_classes = [AsyncThrottle]
    async def get(self, request):
        return JsonResponse({"message": "用户信息!"})


# 异步的用户视图集
class AsyncUserViewSet(ViewSet):
    # 获取用户列表
    async def list(self, requet):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        users = await serializer.adata
        return JsonResponse({"message": "这是异步视图集的list方法", "users": users})

    async def retrieve(self, request, pk):
        user = await User.objects.aget(pk=pk)
        return JsonResponse({"user": {"username": user.username}})


class LoginView(APIView):
    async def post(self, request):
        print(request.headers)
        serializer = AsyncLoginSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            username = validated_data['username']
            password = validated_data['password']
            # authenticate是一个需要查找数据库的阻塞式I/O代码，所以不能直接这样写
            user = await aauthenticate(request, username=username, password=password)
            if user:
                # 这里在用户验证通过后，user对象实际上已经存在内存中了，那么将user对象转换为字典
                # 其实可以不用进行异步等待了，那为什么Serializer类，用于获取异步数据，还要用.adata呢？
                # 这是因为，如果UserSerializer中还定义了有外键参与的字段，那么就需要再次查找数据库了
                # 所以应该用异步版本的.adata来获取数据，更加统一。
                user_serializer = UserSerializer(user)
                user_dict = await user_serializer.adata
                return JsonResponse({"message": "登录成功！", "user": user_dict})
            else:
                return JsonResponse({"message": "用户名或密码错误！"})
        else:
            print(serializer.errors)
            return JsonResponse({"message": "表单校验失败！"})

