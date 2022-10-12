from django.contrib.auth.models import User
from django.db import models

from api.project.models import Project


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Project')
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.TextField(null=True, blank=True, verbose_name='Description')
    time_deadline = models.DateTimeField(verbose_name='Deadline')
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    user_creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
