from django.urls import path
from notes.views import AddNotes, NoteInfo

urlpatterns = [
    path('addNotes', AddNotes.as_view(), name='addNotes'),
    path('noteInfo', NoteInfo.as_view(), name='noteInfo')
]
