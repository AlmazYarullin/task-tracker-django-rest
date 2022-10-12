from rest_framework import serializers

from api.task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'time_deadline', 'user_creator')
