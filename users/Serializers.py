from rest_framework import serializers
from users.models import User
from notes.models import Notes


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone', 'username', 'gender', 'avatar')


class NotesSerializer(serializers.ModelSerializer):
    note_id = serializers.StringRelatedField(source='id')

    class Meta:
        model = Notes
        fields = ('note_id', 'title', 'source', 'link', 'author')
