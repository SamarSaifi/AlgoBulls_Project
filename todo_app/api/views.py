from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from todo_app.models.task import Task
from .serializers import TaskSerializer
from .mixins.filtering import TaskFilterMixin

class TaskViewSet(TaskFilterMixin, viewsets.ModelViewSet):
    """
    ViewSet for managing tasks.
    Provides CRUD operations with filtering capabilities.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]