from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.

class User(AbstractBaseUser):
    """用户表"""
    GENDER = {
        ('1', '男'),
        ('2', '女')
    }
    email = models.CharField(max_length=30, default='', name='email', verbose_name='邮箱')
    phone = models.CharField(max_length=11, default='', unique=True, name='phone', verbose_name='手机号码')
    username = models.CharField(max_length=20, default='', name='username', verbose_name='用户名')
    gender = models.CharField(max_length=10, choices=GENDER, name='gender', default='1', verbose_name='性别')
    avatar = models.ImageField(name='avatar', default='/default/default_head.jpg', verbose_name='头像')

    USERNAME_FIELD = 'phone'

    class Meta:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username + "" + str(self.pk)
