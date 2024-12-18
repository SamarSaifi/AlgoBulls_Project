from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from todo_app.models.task import Task

class TaskAPITests(TestCase):
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
            'tags': ['test']
        }
        
        self.task = Task.objects.create(**self.task_data)

    def test_crud_operations(self):
        # Test Create
        response = self.client.post(
            reverse('task-list'),
            self.task_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Test Read
        response = self.client.get(
            reverse('task-detail', kwargs={'pk': self.task.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task_data['title'])

        # Test Update
        updated_data = {**self.task_data, 'title': 'Updated Task'}
        response = self.client.put(
            reverse('task-detail', kwargs={'pk': self.task.pk}),
            updated_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Task')

        # Test Delete
        response = self.client.delete(
            reverse('task-detail', kwargs={'pk': self.task.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)