from rest_framework import serializers
from abcd.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Todo
        fields= [
            'pk',
            'task',
            'description',
            'cataegory',
            'due_on',
            'time',
        ]