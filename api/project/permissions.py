from django.http import Http404
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request

from .models import Project


class IsOwnerOrMembersReadOnly(BasePermission):
    def has_object_permission(self, request: Request, view, obj: Project):
        if request.method in SAFE_METHODS and obj.members.contains(request.user):
            return False

        if bool(obj.owner == request.user):
            return True
        raise Http404
