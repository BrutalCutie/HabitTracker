from rest_framework.test import APITestCase

from users.models import User


class HabitTestCase(APITestCase):

    def test_create_user(self):
        self.user = User.objects.create(
            telegram_id=1111,
            password='testuser',
            username='testuser',
            email='testuser@testuser.ru'
        )

    def test_create_habit(self):
        data = {
            "telegram_id": 1111,
            "password": 'testuser',
            "username": 'testuser',
            "email": 'testuser@testuser.ru'
        }

        response = self.client.post(
            path='/users/',
            data=data
        )
        self.assertTrue(
            User.objects.all().exists()
        )
        # Делаем заглушки, потому, что пароль хэшируется, а дата меняется
        mock_password = response.json()['password']
        mock_date_joined = response.json()['date_joined']

        self.assertEqual(
            response.json(),
            {'id': 1, 'password': mock_password,
             'last_login': None, 'is_superuser': False, 'first_name': '', 'last_name': '', 'is_staff': False,
             'is_active': False, 'date_joined': mock_date_joined, 'username': 'testuser',
             'email': 'testuser@testuser.ru', 'telegram_id': 1111, 'groups': [], 'user_permissions': []}

        )
