from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.client import RequestFactory
from .models import TaskList, Task, CustomUser
from .serializers import TaskSerializer, TaskListSerializer, LoginSerializer, UserSerializer


class LoginSerializerTest(TestCase):
    def setUp(self):
        self.login_data = {
            'username': 'user1',
            'password': 'password123',
        }

    def test_login_serializer(self):
        serializer = LoginSerializer(data=self.login_data)
        self.assertTrue(serializer.is_valid())


class UserSerializerTest(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'user1',
            'password': 'password123',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'user1@example.com',
            'date_joined': '2022-01-01',
        }

    def test_user_serializer(self):
        serializer = UserSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertIsInstance(user, get_user_model())


class TaskListSerializerTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.task_list_data = {
            'name': 'Task List 1',
            'description': 'This is a task list',
        }
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')

    def test_task_list_serializer(self):
        request = self.factory.post('/api/v1/login/')
        request.user = self.user

        serializer = TaskListSerializer(data=self.task_list_data, context={'request': request})
        self.assertTrue(serializer.is_valid())
        task_list = serializer.save()
        self.assertIsInstance(task_list, TaskList)


class TaskSerializerTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser')
        self.task_list = TaskList.objects.create(name='Task List 2', description='This is a task list', user=self.user)
        self.task_data = {
            'name': 'Task 1',
            'description': 'This is a task',
            'list': self.task_list.id,
    }
        
    def test_task_serializer(self):
        serializer = TaskSerializer(data=self.task_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        task = serializer.save()
        self.assertIsInstance(task, Task)
