from django.db import models


# Create your models here.


class Person(models.Model):

    name = models.CharField(max_length=32, verbose_name='姓名', unique=True, blank=False)
    sex = models.SmallIntegerField(verbose_name='性别', blank=False)
    phone = models.CharField(max_length=11, verbose_name='电话', null=True)
    email = models.CharField(max_length=60, verbose_name='邮箱', null=True)
    address = models.CharField(max_length=60, verbose_name='地址', null=True)
    state = models.CharField(max_length=60, verbose_name='状态', null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
