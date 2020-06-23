from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, **kwargs):
        if not username:
            raise ValueError('必须要传入用户名')
        if not email:
            raise ValueError('必须要传入邮箱')
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password, **kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(username=username, password=password, **kwargs)

    def create_superuser(self, username, password, **kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(username=username, password=password, **kwargs)


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=100, unique=False, verbose_name='密码')
    email = models.EmailField(unique=False, verbose_name='邮箱')

    USERNAME_FIELD = 'username'
    objects = UserManager()

    class Meta:

        # 数据库中生成的表名称 默认是应用名 + 下划线 + 类名
        db_table = 't_user'