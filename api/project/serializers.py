from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False, read_only=True)
    name = serializers.CharField(max_length=20)
    description = serializers.CharField(required=False)
    owner = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )
    members = serializers.SlugRelatedField(
        many=True,
        slug_field='username',
        read_only=True,
    )

    def create(self, validated_data: dict) -> Project:
        members = validated_data.pop('members')
        project = Project.objects.create(**validated_data)
        project.members.set(members)
        return project

    def update(self, instance: Project, validated_data: dict) -> Project:
        members = validated_data.pop('members')
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.members.set(members)
        instance.save()

        return instance
