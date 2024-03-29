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
from .serializers import UserSignupSerializer, UserSerializerLogin, UserSerializerCreate, UserSerializer, ProfileSerializer, ProfileSerializerUpdate
from .models import CustomUser, Profile
from rest_framework.authtoken.models import Token

class HomePageView(TemplateView):
    template_name = 'home.html'

# profiles
class ProfileView(APIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

    @staticmethod
    def get(request):
        """
        List profiles
        """

        profiles = Profile.objects.all()
        return Response(ProfileSerializer(profiles, many=True).data)


# profiles/{profile_id}
class ProfileDetail(APIView):

    @staticmethod
    def patch(request, profile_id):
        """
        Update profile of authenticated user
        """

        profile = get_object_or_404(Profile, pk=profile_id)
        if profile.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = ProfileSerializerUpdate(profile, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            profile = serializer.save()
            return Response(UserSerializerLogin(profile.user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#class UserListView(generics.ListCreateAPIView):
class UserListView(APIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


    @staticmethod
    def get(request):
        """
        List users
        """

        users = CustomUser.objects.all()
        return Response(UserSerializer(users, many=True).data)

    @staticmethod
    def post(request):
        """
        Create user
        """

        serializer = UserSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()
            Profile(user=user).save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#class UserDetail(APIView):
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

    @staticmethod
    #def get(request, user_id):
    def get(request, pk):

        """
        View individual user
        """

        #user = get_object_or_404(CustomUser, pk=user_id)
        user = get_object_or_404(CustomUser, pk=pk)
        return Response(UserSerializer(user).data)

    @staticmethod
    def patch(request, pk):
    #def put(request, pk):
        """
        Update authenticated user
        """

        user = get_object_or_404(CustomUser, pk=pk)
        if user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = UserSerializerUpdate(user, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(UserSerializerLogin(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, user_id):
        """
        Delete user
        """

        user = get_object_or_404(CustomUser, pk=user_id)
        if is_administrator(user) or user.is_superuser:
            return Response({
                constants.ERROR: 'That user can not be deleted'
            }, status=status.HTTP_401_UNAUTHORIZED)
        if is_moderator(user) and not is_administrator(request.user):
            return Response({
                constants.ERROR: 'Admin permissions needed to delete moderators'
            }, status=status.HTTP_401_UNAUTHORIZED)
        if not is_moderator(request.user):
            return Response({
                constants.ERROR: 'Moderator permissions needed to delete users'
            }, status=status.HTTP_401_UNAUTHORIZED)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
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

def user_create(request):
    
    ret = HttpResponse('ok')
    # 允许http://127.0.0.1:8001域向我发请求
    ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    if request.method == 'OPTIONS':
        # 所有的头信息都允许
        ret['Access-Control-Allow-Headers'] = '*'
    return ret
        # print(request.POST)
    serializer = UserSignupSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        user = serializer.save()
        return Response(UserSerializerLogin(user).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    username = request.POST.get('username')
    password = request.POST.get('password')
    email  = request.POST.get('email')
    print(username, password, email)
    print(type(username), type(password),type(email))
    user = get_object_or_404(CustomUser, username=request.data.get('username'))
    user = authenticate(username=user.username, password=request.data.get('password'))
    token = user.token
    if user:
        #serializer = UserSerializerLogin(user)
            
        #if (account == 'admin') and (password == '123456'):

        serializer = UserSerializerLogin(user)
        ret = Response(serializer.data)
        ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    else:
        ret = HttpResponse('error', status=status.HTTP_400_BAD_REQUEST)
        ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'

    return ret


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
   # ret = HttpResponse('ok')
    # 允许http://127.0.0.1:8001域向我发请求
   # ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    #if request.method == 'OPTIONS':
        # 所有的头信息都允许
     #   ret['Access-Control-Allow-Headers'] = '*'
      #  return ret
    # print(request.POST)
   # account = request.POST.get('account')
   # password = request.POST.get('password')
   # print(account, password)
   # print(type(account), type(password))
   # token = 'admin123456'
   # if (account == 'admin') and (password == '123456'):

        #ret = HttpResponse(json.dumps({'token': token}))
        #ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    #else:
     #   ret = HttpResponse('error', status=402)
      #  ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'

   # return ret

    ret = HttpResponse('ok')
    # 允许http://127.0.0.1:8001域向我发请求
    ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    if request.method == 'OPTIONS':
        # 所有的头信息都允许
        ret['Access-Control-Allow-Headers'] = '*'
    return ret
        # print(request.POST)
    username = request.POST.get('account')
    password = request.POST.get('password')
    print(username, password)
    print(type(username), type(password))
    user = get_object_or_404(CustomUser, username=request.data.get('username'))
    user = authenticate(username=user.username, password=request.data.get('password'))
    token = user.token
    if user:
        #serializer = UserSerializerLogin(user)
            
        #if (account == 'admin') and (password == '123456'):

        serializer = UserSerializerLogin(user)
        ret = Response(serializer.data)
        ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    else:
        ret = HttpResponse('error', status=status.HTTP_400_BAD_REQUEST)
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
