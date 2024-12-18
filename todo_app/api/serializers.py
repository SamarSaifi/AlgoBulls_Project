from rest_framework import serializers
from todo_app.models.task import Task
from todo_app.utils.tag_helpers import clean_tags
from .mixins.validation import TaskValidationMixin

class TaskSerializer(TaskValidationMixin, serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'timestamp', 'title', 'description', 'due_date', 'tags', 'status']
        read_only_fields = ['timestamp']

    def validate_tags(self, value):
        return clean_tags(value) if value else []