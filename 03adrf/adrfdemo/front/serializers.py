from adrf.serializers import Serializer, ModelSerializer
from rest_framework import fields
import re
from django.contrib.auth import get_user_model

User = get_user_model()


class AsyncLoginSerializer(Serializer):
    username = fields.CharField(max_length=20)
    password = fields.CharField(min_length=6, max_length=20, error_messages={"min_length": "密码长度最少为6位！"})

    def validate(self, attrs):
        username = attrs['username']
        pattern = re.compile(r'^[a-zA-Z][a-zA-Z0-9_]{4,19}$')
        if pattern.match(username):
            return attrs
        else:
            raise fields.ValidationError("用户名不符合规则！")


# class UserSerializer(Serializer):
#     username = fields.CharField(max_length=200)
#     email = fields.EmailField()
#     is_active = fields.BooleanField()
#     is_staff = fields.BooleanField()
    # department = DepartmentSerializer()

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'is_active']