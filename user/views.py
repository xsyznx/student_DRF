from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class LoginView(APIView):

    def get(self, request, format=None):

        return Response({'code': 0, 'message': '登录成功'})