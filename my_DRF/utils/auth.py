from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from AuthDemo.models import UserInfo


class Myauth(BaseAuthentication):
    def authenticate(self, request):
        # 获取前端带来的token
        # 对比数据库中的token是否合法
        token = request.query_params.get('token', '')
        if not token:
            raise AuthenticationFailed('没有携带token')
        user_obj = UserInfo.objects.filter(token=token).first()
        if user_obj:
            return (user_obj, token)
        raise AuthenticationFailed('token不合法')
