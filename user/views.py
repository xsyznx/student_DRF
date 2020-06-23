from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from django.http.response import HttpResponse
from django.contrib.auth import authenticate


def create(request):
    username = 'smart'
    password = 'smart'
    email = 'email'
    user = User.objects.create_user(username=username, password=password, email=email)
    return HttpResponse('成功')


class RegisterView(APIView):

    def get(self, request, format=None):

        return Response({'code': 0, 'message': '注册成功'})

    def post(self, request, format=None):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if not all([username, password, email]):
            return Response({'code': 1, 'message': '数据不完整'})
        user = User.objects.create_user(username=username, password=password, email=email)
        if user:
            return Response({'code': 0, 'message': '注册成功'})
        return Response({'code': 2, 'message': '注册失败'})


class LoginView(APIView):

    def get(self, request, format=None):

        return Response({'code': 0, 'message': '登录成功'})

    def post(self, request, format=None):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not all([username, password]):
            return Response({'code': 1, 'message': '数据不完整'})
        user = authenticate(request, username=username, password=password)
        if user:
            return Response({'code': 0, 'message': '登录成功'})
        else:
            return Response({'code': 2, 'message': '用户名或密码错误'})


def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    return {
        'token': token,
        'user_id': user.id,
        'username': user.username
    }