from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'timestamp', 'title', 'description', 'due_date', 'tags', 'status']
        read_only_fields = ['timestamp']

    def validate_tags(self, value):
        if value:
            # Remove duplicates while preserving order
            return list(dict.fromkeys(value))
        return value

    def validate(self, data):
        if 'due_date' in data and data['due_date']:
            if self.instance and data['due_date'] < self.instance.timestamp:
                raise serializers.ValidationError(
                    "Due date cannot be before creation timestamp"
                )
        return data