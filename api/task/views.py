from rest_framework.exceptions import NotFound
from rest_framework.viewsets import ModelViewSet

from api.project.models import Project
from api.task.models import Task
from api.task.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        project_pk = self.kwargs.get('project_pk')
        project = Project.objects.get(pk=project_pk)
        return self.queryset.filter(project=project)

    def perform_create(self, serializer):
        project = Project.objects.get(pk=self.kwargs.get('project_pk'))
        serializer.save(project=project)
