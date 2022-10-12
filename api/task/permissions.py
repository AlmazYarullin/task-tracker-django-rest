from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from .models import Task


class IsProjectMember(BasePermission):
    def has_object_permission(self, request: Request, view, obj: Task):
        return obj.project.members.contains(request.user)
