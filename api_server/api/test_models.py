from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import TaskList, Task, CustomUser

# Model tests
class CustomUserTest(TestCase):
    def setUp(self):
        # Instance the user
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
            first_name='Test',
            last_name='User'
        )
    
    def test_create_custom_user_with_required_fields(self):
        # Validate yours datas
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')

        # Check password
        self.assertTrue(self.user.check_password('testpassword'))

        # Test if user is none
        self.assertIsNotNone(self.user)

    def test_create_custom_user_without_email(self):
        try:
            self.user = CustomUser.objects.create_user(
                username='newest_user',
                password='newestpassword'
            ).clean_fields()
            self.fail('ValidationError not raised')
        except ValidationError as e:
            self.assertEqual(e.message_dict['email'][0], 'This field cannot be blank.')


class TaskListTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.task_list = TaskList.objects.create(
            name='Test Task List',
            description='Test Description',
            user=self.user
        )

    def test_task_list_creation(self):
        self.assertEqual(self.task_list.name, 'Test Task List')
        self.assertEqual(self.task_list.description, 'Test Description')
        self.assertEqual(self.task_list.user, self.user)


class TaskTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.task_list = TaskList.objects.create(
            name='Test Task List',
            description='Test Description',
            user=self.user
        )
        self.task = Task.objects.create(
            name='Test Task',
            description='Test Description',
            is_complete=False,
            due_date=None,
            parent_task=None,
            list=self.task_list
        )

    def test_task_creation(self):
        self.assertEqual(self.task.name, 'Test Task')
        self.assertEqual(self.task.description, 'Test Description')
        self.assertFalse(self.task.is_complete)
        self.assertIsNone(self.task.due_date)
        self.assertIsNone(self.task.parent_task)
        self.assertEqual(self.task.list, self.task_list)