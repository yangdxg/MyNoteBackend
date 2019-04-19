from django.db import models
from datetime import datetime
from users.models import User


# Create your models here.

class Notes(models.Model):
    """笔记model"""
    link = models.CharField(max_length=300, verbose_name='连接地址', default="")
    title = models.CharField(max_length=50, verbose_name='标题', default="")
    author = models.CharField(max_length=30, verbose_name='作者', default="")
    source = models.CharField(max_length=30, verbose_name='来源', default="")
    content = models.TextField(verbose_name="内容", default="")
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    last_read_time = models.DateTimeField(default=datetime.now, verbose_name='上次阅读时间')
    user = models.ForeignKey(null=True, blank=True, on_delete=models.SET_NULL, to=User, verbose_name='添加人')

    class Meta:
        db_table = 'notes'
        verbose_name = '笔记'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
