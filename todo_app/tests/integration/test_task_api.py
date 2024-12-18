from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from todo_app.models.task import Task
from django.utils import timezone
from datetime import timedelta

class TaskAPIIntegrationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
        
        self.task_data = {
            'title': 'Test Task',
            'description': 'Test Description',
            'tags': ['test'],
            'due_date': (timezone.now() + timedelta(days=1)).isoformat()
        }

    def test_task_lifecycle(self):
        # Create
        response = self.client.post(
            reverse('task-list'),
            self.task_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        task_id = response.data['id']

        # Read & Verify
        response = self.client.get(reverse('task-detail', kwargs={'pk': task_id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task_data['title'])

        # Update
        updated_data = {**self.task_data, 'title': 'Updated Task'}
        response = self.client.put(
            reverse('task-detail', kwargs={'pk': task_id}),
            updated_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Task')

        # Filter
        response = self.client.get(f"{reverse('task-list')}?status=OPEN")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        # Delete
        response = self.client.delete(reverse('task-detail', kwargs={'pk': task_id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)