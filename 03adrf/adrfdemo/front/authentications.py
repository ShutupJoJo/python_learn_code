from rest_framework.authentication import BaseAuthentication, get_authorization_header
from django.contrib.auth import get_user_model
from rest_framework import exceptions

User = get_user_model()


class AsyncAuthentication(BaseAuthentication):
    keyword = 'JWT'

    async def authenticate(self, request):
        # Authorization: JWT xxx
        auth = get_authorization_header(request).split()
        token = auth[1].decode('utf-8')
        if token == 'zhiliao':
            user = await User.objects.afirst()
            setattr(request, 'user', user)
            return user, token
        else:
            raise exceptions.ValidationError("JWToken验证失败！")

