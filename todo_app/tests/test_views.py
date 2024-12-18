from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from ..models import Task

class TaskViewSetTests(TestCase):
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

    def test_create_task(self):
        response = self.client.post(
            reverse('task-list'),
            self.task_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_get_task_list(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_task_detail(self):
        response = self.client.get(
            reverse('task-detail', kwargs={'pk': self.task.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task_data['title'])

    def test_update_task(self):
        updated_data = {
            'title': 'Updated Task',
            'description': self.task_data['description'],
            'tags': self.task_data['tags']
        }
        response = self.client.put(
            reverse('task-detail', kwargs={'pk': self.task.pk}),
            updated_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Task')

    def test_delete_task(self):
        response = self.client.delete(
            reverse('task-detail', kwargs={'pk': self.task.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)