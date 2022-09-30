from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False, read_only=True)
    name = serializers.CharField(max_length=20)
    description = serializers.CharField(required=False)

    def create(self, validated_data: dict) -> Project:
        return Project.objects.create(**validated_data)

    def update(self, instance: Project, validated_data: dict) -> Project:
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
