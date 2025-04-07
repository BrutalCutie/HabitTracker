from rest_framework.test import APITestCase
from unittest.case import TestCase

from tracker.models import Habit
from tracker.tasks import remind_controler
from users.models import User


class HabitTestCase(APITestCase):
    user = None

    def setUp(self):
        self.user = User.objects.create(
            telegram_id=1111,
            password='testuser',
            username='testuser',
            email='testuser@testuser.ru'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        data = {
            "action": "Выпить воды",
            "publish_to_all": True,
            "reward": "Скушать печенюшку",
            "time": "10-00",
            "time_to_complete": 120,
            "place": "Работа"

        }

        response = self.client.post(
            path='/habits/',
            data=data
        )
        self.assertTrue(
            Habit.objects.all().exists()
        )
        self.assertEqual(
            response.json(),
            {'id': 1, 'place': 'Работа', 'time': '10:00:00', 'action': 'Выпить воды', 'is_nice_habit': False,
             'periodicity': 1440, 'reward': 'Скушать печенюшку', 'time_to_complete': '00:02:00',
             'publish_to_all': True, 'owner': 1, 'chained_habit': None, 'last_notification': None}

        )

    def test_delete_habit(self):

        data = {
            "action": "Выпить воды",
            "publish_to_all": True,
            "reward": "Скушать печенюшку",
            "time": "10-00",
            "time_to_complete": 120,
            "place": "Работа"

        }
        response = self.client.post(
            path='/habits/',
            data=data
        )

        # забираем id отдельно, потому что он может меняться в зависимости от тестов
        created_habit_id = response.json()['id']

        self.assertTrue(Habit.objects.get(pk=created_habit_id))

        Habit.objects.get(pk=created_habit_id).delete()

        self.assertFalse(Habit.objects.all())


class TasksTestCase(TestCase):
    def test_remind_controler(self):
        self.assertEqual(remind_controler(), None)
