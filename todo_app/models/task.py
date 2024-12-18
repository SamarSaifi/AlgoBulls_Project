from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField
from todo_app.utils.validators import validate_future_date, validate_string_length
from todo_app.utils.tag_helpers import clean_tags
from .task_status import TaskStatus

class Task(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    due_date = models.DateTimeField(null=True, blank=True)
    tags = ArrayField(
        models.CharField(max_length=50),
        blank=True,
        default=list
    )
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.OPEN
    )

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.title} ({self.status})"

    def clean(self):
        self._validate_fields()
        self._clean_tags()

    def _validate_fields(self):
        validate_string_length(self.title, 100, "Title")
        validate_string_length(self.description, 1000, "Description")
        if self.due_date:
            validate_future_date(self.due_date)

    def _clean_tags(self):
        self.tags = clean_tags(self.tags)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)