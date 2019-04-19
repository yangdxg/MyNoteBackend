from rest_framework import views
from django.http import HttpResponse, JsonResponse
from users.Serializers import UserSerializer
from users.Serializers import NotesSerializer
from users.models import User
from notes.models import Notes

import json


# Create your views here.
# class Users(views.APIView):

class Register(views.APIView):
    def get(self, request):
        return HttpResponse(json.dumps({'success': 0}))

    def post(self, request):
        phone = request.data['phone']
        username = phone
        password = request.data['password']
        if phone == '':
            return HttpResponse(json.dumps({
                'status': 1,
                'message': '手机号不能为空'
            }))
        elif (username == '') | (password == ''):
            return HttpResponse(json.dumps({
                'status': 1,
                'message': '用户名或密码不能为空'
            }))
        else:
            users = User.objects.filter(phone=phone)
            if len(users) > 0:
                return HttpResponse(json.dumps({
                    'status': 1,
                    'message': '该手机号已注册'
                }))
            else:
                user = User(phone=phone, username=username, password=password)
                print(user)
                user.save()
                serializer = UserSerializer(user)
                print(serializer.data)
                return HttpResponse(json.dumps({
                    'status': 0,
                    'message': '注册成功',
                    'data': serializer.data
                }))


class Login(views.APIView):
    def post(self, request):
        phone = request.data['phone']
        password = request.data['password']
        users = User.objects.filter(phone=phone)
        if len(users) == 0:
            return HttpResponse(json.dumps({
                'status': 1,
                'message': '该手机号未注册'
            }))
        elif users[0].password != password:
            print(users[0].password)
            print(password)
            return HttpResponse(json.dumps({
                'status': 1,
                'message': '密码错误'
            }))
        else:
            user = users[0]
            userJson = {
                'phone': user.phone,
                'username': user.username,
                'gender': user.gender,
                'avatar': str(user.avatar)
            }
            return HttpResponse(json.dumps({
                'status': 0,
                'data': userJson
            }))


class MyNotes(views.APIView):
    def get(self, request):
        user_id = request.GET['user_id']
        users = User.objects.filter(pk=user_id)
        if len(users) == 0:
            return HttpResponse(json.dumps({
                'status': 1,
                'message': '用户不存在'
            }))
        else:
            notes = Notes.objects.filter(user=users[0]).order_by('-last_read_time')
            notes_Serializers = NotesSerializer(notes, many=True)
            return HttpResponse(json.dumps({
                'status': 0,
                'data': notes_Serializers.data
            }))
