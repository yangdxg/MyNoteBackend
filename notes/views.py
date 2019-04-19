from django.shortcuts import render
from rest_framework import views
from django.http import HttpResponse, JsonResponse
from notes.models import Notes
from users.models import User
from notes.serializers import NotesSerializer
import json

from notes.parse import ParseLink


# Create your views here.

class AddNotes(views.APIView):
    def post(self, request):
        link = request.data['link']
        user_id = request.data['user_id']
        user = User.objects.filter(pk=user_id)[0]
        notes = Notes.objects.filter(user=user)
        # for note in notes:
        # if note.link == link:
        #     return HttpResponse(json.dumps({
        #         'state': 2,
        #         'message': '该文章已经添加了'
        #     }))

        title, author, source, content = ParseLink().parse(link=link)
        print(title)
        print(author)
        print(source)
        # print(content)
        if content is None:
            print("空的 ")
        else:
            print("没问题")
        note = Notes(link=link, title=title, author=author, source=source, content=content, user=user)
        print(note)
        note.save()
        return HttpResponse(json.dumps({
            'state': 0,
            'message': '保存成功'
        }))


class NoteInfo(views.APIView):
    def get(self, request):
        note_id = request.GET['note_id']
        if note_id != '':
            note = Notes.objects.get(id=note_id)
            print(note)
            serializer = NotesSerializer(note, many=False)
            print(serializer.data)
            return HttpResponse(json.dumps({
                'status': 0,
                'data': serializer.data
            }))
