#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'MacVSPC'
__mtime__ = '2018/6/7'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from django.contrib import admin
from django.urls import path,re_path
from boycott import views
app_name='boycott'
urlpatterns = [
    path(r'index/', views.index,name='index'),  #第一啊个参数还不能写 index.html
    path(r'login/', views.login,name='login'),
    path(r'list/<int:id>/', views.list,{'iid':222},name='list'),  #可自定义参数顺序  给参数id设置默认值    第一个参数不写，那就不会显示list出来了！！！
    path(r'register/', views.register),  #可自定义参数顺序  给参数id设置默认值    第一个参数不写，那就不会显示list出来了！！！
    # 上面要有name，否则找不到执行的函数
    re_path(r'^list/(?P<id>[0-9]+)/(?P<iid>[0-9]+)/$', views.list,name='list'),   #这里一定要加条件，若是没有[0-9]+ 则不会执行
    path(r'index/delete/', views.delete,name='delete'),
    path('ajaxTot/', views.ajaxTot,name='ajaxTot'),
    # path(r'^list/(?P<id>\d)/(?P<iid>\d)$', list), #这是老版本的写法 理解错了   re_path(r'^bio/(?P<username>\w+)/$', views.bio, name='bio'),
]