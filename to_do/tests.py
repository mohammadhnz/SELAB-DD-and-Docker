from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task

class TaskAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_task(self):
        response = self.client.post('/tasks/', {'title': 'Test Task', 'description': 'Testing', 'due_date': '2023-08-30T12:00:00Z'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')

    def test_get_tasks(self):
        Task.objects.create(title='Task 1', description='Description 1', due_date='2023-08-30T12:00:00Z')
        Task.objects.create(title='Task 2', description='Description 2', due_date='2023-08-31T12:00:00Z')

        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_task(self):
        task = Task.objects.create(title='Task', description='Description', due_date='2023-08-30T12:00:00Z')
        response = self.client.put(f'/tasks/{task.id}/', {'title': 'Updated Task', 'description': 'Updated Description', 'due_date': '2023-09-01T12:00:00Z'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get().title, 'Updated Task')

    def test_delete_task(self):
        task = Task.objects.create(title='Task', description='Description', due_date='2023-08-30T12:00:00Z')
        response = self.client.delete(f'/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
