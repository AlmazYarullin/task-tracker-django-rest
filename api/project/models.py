from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    description = models.TextField(null=True, blank=True, verbose_name='Description')
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    members = models.ManyToManyField(User, related_name='members', related_query_name='members')
