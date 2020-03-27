# Create your views here.
from django.http import HttpResponse
import sqlite3
import json
import copy
import os
from django.views.generic import TemplateView, View
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from .serializers import UserSignupSerializer, UserSerializerLogin
from .models import CustomUser

class HomePageView(TemplateView):
    template_name = 'home.html'
class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSignupSerializer

    @staticmethod
    def post(request):
        """
        create user
        """

        serializer = UserSignupSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializerLogin(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializerLogin

    @staticmethod
    def post(request):
        """
        Get user data and API token
        """
 
        user = get_object_or_404(CustomUser, username=request.data.get('username'))
        user = authenticate(username=user.username, password=request.data.get('password'))
        if user:
            serializer = UserSerializerLogin(user)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
 




def login(request):
    ret = HttpResponse('ok')
    # 允许http://127.0.0.1:8001域向我发请求
    ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    if request.method == 'OPTIONS':
        # 所有的头信息都允许
        ret['Access-Control-Allow-Headers'] = '*'
        return ret
    # print(request.POST)
    account = request.POST.get('account')
    password = request.POST.get('password')
    print(account, password)
    print(type(account), type(password))
    token = 'admin123456'
    if (account == 'admin') and (password == '123456'):

        ret = HttpResponse(json.dumps({'token': token}))
        ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    else:
        ret = HttpResponse('error', status=402)
        ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'

    return ret


def get_photo(request):
    print('获取图片:', request.path[1:])
    with open(request.path[1:], "rb") as f:
        photo = f.read()
    return HttpResponse(photo, content_type="image/jpg")


def get_list(request):
    conn = sqlite3.connect('userManagement.db')  # 连接数据库
    cur = conn.cursor()  # 创建游标
    cur.execute('select * from userData')

    data = list()
    item_dict = dict()
    for item in cur.fetchall():
        item_dict['date'] = item[0]
        item_dict['name'] = item[1]
        item_dict['tel'] = item[2]
        item_dict['addr'] = item[3]
        item_dict['desc'] = item[4]
        data.append(copy.deepcopy(item_dict))
    ret = HttpResponse(json.dumps(data))
    conn.commit()  # 提交事务
    cur.close()
    conn.close()  # 关闭连接
    # 允许http://127.0.0.1:8001域向我发请求
    ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    if request.method == 'OPTIONS':
        # 所有的头信息都允许
        ret['Access-Control-Allow-Headers'] = '*'

    return ret


def remove_user(request):
    req = request.GET
    conn = sqlite3.connect('userManagement.db')  # 连接数据库
    cur = conn.cursor()  # 创建游标

    cur.execute("DELETE FROM userData WHERE name = '{}'".format(req['name']))
    ret = HttpResponse("success")

    conn.commit()  # 提交事务
    cur.close()
    conn.close()  # 关闭连接
    # 允许http://127.0.0.1:8001域向我发请求
    ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    if request.method == 'OPTIONS':
        # 所有的头信息都允许
        ret['Access-Control-Allow-Headers'] = '*'

    return ret


def edit_user(request):
    req = request.GET
    conn = sqlite3.connect('userManagement.db')  # 连接数据库
    cur = conn.cursor()  # 创建游标

    cur.execute(
        "UPDATE userData SET date='{0}', tel='{1}', addr='{2}', desc='{3}' WHERE name = '{4}'"
            .format(req['date'], req['tel'], req['addr'], req['desc'], req['name']))

    ret = HttpResponse("success")

    conn.commit()  # 提交事务
    cur.close()
    conn.close()  # 关闭连接
    # 允许http://127.0.0.1:8001域向我发请求
    ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    if request.method == 'OPTIONS':
        # 所有的头信息都允许
        ret['Access-Control-Allow-Headers'] = '*'

    return ret


def add_user(request):
    req = request.GET
    conn = sqlite3.connect('userManagement.db')  # 连接数据库
    cur = conn.cursor()  # 创建游标
    cur.execute('INSERT INTO userData (date, name, tel, addr, desc) VALUES (?, ?, ?, ?, ?)',
                (req['date'], req['name'], req['tel'], req['addr'], req['desc']))

    conn.commit()  # 提交事务
    cur.close()
    conn.close()  # 关闭连接
    ret = HttpResponse('success')
    # 允许http://127.0.0.1:8001域向我发请求
    ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    if request.method == 'OPTIONS':
        # 所有的头信息都允许
        ret['Access-Control-Allow-Headers'] = '*'

    return ret


def upload(request):
    ret = HttpResponse('success')
    # 允许http://127.0.0.1:8001域向我发请求
    ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    # 所有的头信息都允许
    ret['Access-Control-Allow-Headers'] = '*'
    if request.method == 'OPTIONS':
        print("收到options的请求")
        return ret
    print(request.POST.get('file'))
    # for k, v in dict(request.POST).items():
    #     print(k, v)
    with open('./photos/{}.jpg'.format(request.POST['name']), 'wb+') as f:
        f.write(request.FILES.get('file').read())
    return ret


def get_advertisement_list(request):
    # for root, dirs, files in os.walk('photos'):
    data = os.listdir('photos')
    # data = ['wf1.jpg', 'wf2.jpg', 'wf3.jpg', '1.jpg']
    ret = HttpResponse(json.dumps(data))
    # 允许http://127.0.0.1:8001域向我发请求
    ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    if request.method == 'OPTIONS':
        # 所有的头信息都允许
        ret['Access-Control-Allow-Headers'] = '*'
    return ret
