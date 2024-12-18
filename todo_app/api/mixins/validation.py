from rest_framework import serializers
from django.utils import timezone

class TaskValidationMixin:
    def validate_title(self, value):
        if len(value) > 100:
            raise serializers.ValidationError("Title must be less than 100 characters")
        return value

    def validate_description(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError("Description must be less than 1000 characters")
        return value

    def validate_due_date(self, value):
        if value and value < timezone.now():
            raise serializers.ValidationError("Due date cannot be in the past")
        return value