from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from todo_app.models.task import Task
from todo_app.models.task_status import TaskStatus

class TaskModelTests(TestCase):
    def setUp(self):
        self.valid_task_data = {
            'title': 'Test Task',
            'description': 'Test Description',
            'due_date': timezone.now() + timedelta(days=1),
            'tags': ['test', 'unit-test']
        }

    def test_create_task(self):
        task = Task.objects.create(**self.valid_task_data)
        self.assertEqual(task.title, self.valid_task_data['title'])
        self.assertEqual(task.status, TaskStatus.OPEN)

    def test_validation(self):
        # Test title length
        with self.assertRaises(ValidationError):
            Task.objects.create(
                title='a' * 101,
                description='Test Description'
            )

        # Test description length
        with self.assertRaises(ValidationError):
            Task.objects.create(
                title='Test Title',
                description='a' * 1001
            )

        # Test due date validation
        with self.assertRaises(ValidationError):
            Task.objects.create(
                title='Test Title',
                description='Test Description',
                due_date=timezone.now() - timedelta(days=1)
            )