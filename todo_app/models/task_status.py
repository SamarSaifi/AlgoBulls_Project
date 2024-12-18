from django.db import models

class TaskStatus(models.TextChoices):
    OPEN = 'OPEN', 'Open'
    WORKING = 'WORKING', 'Working'
    PENDING_REVIEW = 'PENDING_REVIEW', 'Pending Review'
    COMPLETED = 'COMPLETED', 'Completed'
    OVERDUE = 'OVERDUE', 'Overdue'
    CANCELLED = 'CANCELLED', 'Cancelled'