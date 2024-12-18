from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField

class TaskStatus(models.TextChoices):
    OPEN = 'OPEN', 'Open'
    WORKING = 'WORKING', 'Working'
    PENDING_REVIEW = 'PENDING_REVIEW', 'Pending Review'
    COMPLETED = 'COMPLETED', 'Completed'
    OVERDUE = 'OVERDUE', 'Overdue'
    CANCELLED = 'CANCELLED', 'Cancelled'

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

    def clean(self):
        if self.due_date and self.due_date < self.timestamp:
            raise ValidationError("Due date cannot be before creation timestamp")
        
        # Ensure unique tags
        if self.tags:
            self.tags = list(set(self.tags))

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.status})"