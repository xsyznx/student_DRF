from django.urls import path
from django.conf.urls import url
from .views import LoginView, RegisterView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'authenticate', obtain_jwt_token),
    url(r'login', LoginView.as_view(), name='login'),
    url(r'register', RegisterView.as_view(), name='register'),
]
