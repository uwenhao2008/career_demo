from django.shortcuts import render
from django.http.response import HttpResponse
# from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import render
# from boycott.models import *
from boycott import models

from django.http import HttpResponse
import re


# Create your views here.
def index(res):
    ret = {'data': None, 'group': None}  # 大哥  这里用等号  不是冒号 ： !!!!~~~~~~~~~~~
    usergroup = models.UserGroup.objects.all()
    # usergroup = models.UserGroup.objects.filter(asset__bDel=1)
    # where条件怎么实现？  0的不显示
    ret['group'] = usergroup
    if res.method == 'POST':
        hostname = res.POST.get('hostname', None)
        ip = res.POST.get('m_ip', '8.8.8.88')
        user_group = res.POST.get('usergroup', None)
        models.Asset.objects.create(hostname=hostname, ip=ip, user_group_id=user_group)
    # return render_to_response('boycott/index.html',{})  #CSRF verification failed. Request aborted.  这个语法是老的，可能会出现左边这个报错
    data = models.Asset.objects.filter(bDel=1)
    # print(data.query)
    ret['data'] = data
    return render(res, 'boycott/index.html', ret)  # CSRF verification failed. Request aborted.


def login(res):
    print(res)
    ret = {'status': '初始化变量'}
    if res.method == 'POST':
        username = res.POST.get('username', None)
        password = res.POST.get('password', None)
        print(username, password)  # 数据是正常传输的
        is_auth = all([username, password])
        print(is_auth)  # 只有都输入的才进行匹配处理
        if is_auth:
            count = models.Userinfo.objects.filter(username=username, password=password).count()
            # print(models.Userinfo.objects.all().values('password'))  #输出password列
            #   from django.db import models
            #   count = models.Userinfo.objects.filter(username=username,password=password).count()
            #   我这里出问题，就是因为import错了错误的对象，导致django.db.models没有Userinfo属性
            # print(count)
            if count == 1:
                # return HttpResponseRedirect("https://www.baidu.com/")
                return HttpResponseRedirect("/boycott/index")
                # ret['status'] = 'Success'
            else:
                ret['status'] = '用户名或密码错误'
        else:
            ret['status'] = '用户名或密码不能为空'
    # response = HttpResponse(ret, content_type='application/vnd.ms-excel')
    # print(response)
    # response['Content-Disposition'] = 'attachment; filename="foo.xls"'
    return render(res, 'boycott/login.html', {'status': ret['status']})  # 麻痹的 调试那么久。是这里写错了  botcott/login  而且路径要对


# https://docs.djangoproject.com/en/2.0/ref/request-response/

def list(res, id, iid):
    print(id, iid)
    return HttpResponse('list/' + str(id) + '/' + str(iid))


def register(self):
    t1 = models.UserType.objects.create(name='超级管理员')
    t2 = models.UserType.objects.create(name='普通管理员')

    t3 = models.UserType.objects.get(name='普通管理员')
    u3 = models.Userinfo.objects.create(username='wenhao', password='123', user_type=t3)

    t4 = models.UserType.objects.get(name='超级管理员')
    u4 = models.Userinfo.objects.create(username='leilei', password='123', user_type=t4)

    groupObjA = models.UserGroup.objects.create(GroupName='用户组A')
    groupObjB = models.UserGroup.objects.create(GroupName='用户组B')

    groupObjA.user.add(u3)
    groupObjB.user.add(u4)
    return HttpResponse("创建数据成功")


def delete(res):
    return HttpResponse('<h1>Head</h1>')


def ajaxTot(res):
    ret = {'id':None,'status':None,'ip':None}
    print(res.GET)
    # print(res.POST)
    ret['id'],ret['ip'] = res.GET.get('p'),res.GET.get('q')

    #根据接收到的 p 把数据库对应的 bDel修改为  0  看页面是否有效果


    if re.match('del_id_',str(ret['id']),flags=0):   #这里需要把参数转字符串，否则会报错
        # return render(res, 'boycott/ajaxTot.html', ret)   #这里必须写 'boycott/ajaxTot.html'  后缀去掉以后就报错

        # return HttpResponseRedirect('/boycott/ajaxTot.html')
        return HttpResponseRedirect('/boycott/ajaxTot')   #这句就正常执行，上面的就不行  why？

        # return HttpResponseRedirect("https://www.baidu.com/")  #同源策略，所以这里不能执行，需要结合jsonp
    else:
        return HttpResponse('<h1>ajax is NOT OK!</h1>')
