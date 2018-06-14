from django.db import models

# Create your models here.
class UserType(models.Model):
    name = models.CharField(max_length=50)

class Userinfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    memo = models.CharField(max_length=50)
    user_type = models.ForeignKey('UserType',on_delete=models.CASCADE)
    # 2.0 后 定义外键和一对一关系的时候需要加on_delete选项

class UserGroup(models.Model):
    GroupName = models.CharField(max_length=50)
    user = models.ManyToManyField('Userinfo')

class Asset(models.Model):
    hostname = models.CharField(max_length=50)
    ip = models.GenericIPAddressField()
    user_group = models.ForeignKey('UserGroup',on_delete=models.CASCADE)
    bDel = models.CharField(max_length=10,default=1)  #为0 就认为是删除了



