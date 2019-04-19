from rest_framework import serializers
from notes.models import Notes


class NotesSerializer(serializers.ModelSerializer):
    # note_id = serializers.StringRelatedField(source='id')

    class Meta:
        model = Notes
        fields = ('title','content')
