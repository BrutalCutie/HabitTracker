import datetime
import requests
from rest_framework import status

from config.settings import TG_BOT_TOKEN
from tracker.models import Habit


class HabitTimeControl:
    """Контроллер для полезных привычек"""
    __slots__ = ['habit_time', 'local_datetime']

    def __init__(self, habit_time: datetime.time):
        self.habit_time: datetime.datetime.time = habit_time
        self.local_datetime: datetime.datetime = datetime.datetime.now()

    def time_control(self) -> bool | None:
        """
        Проверка на совпадение времени между текущим и времени привычки
        :return:
        """
        if not self.habit_time:  # Вернуть None если по какой-то причине время не передалось в привычку
            return None

        return self.habit_time.strftime("%H:%M") == self.local_datetime.time().strftime("%H:%M")  # True или False

    def is_today_notification(self, habit_last_notification: datetime.datetime, periodicity: int) -> bool:
        """
        Проверка на совпадение датыВремени между текущей и датойВременем привычки

        :param habit_last_notification: датаВремя привычки
        :param periodicity: перидичность, с которой должны приходить уведомления(в минутах)
        :return:
        """
        # проверка на None. None у привычки в "последнем уведомлении" присваивается при создании.
        if habit_last_notification is None:
            return True

        # датаВремя, когда должно отсылаться следующее уведомление
        notification_must_be_at = habit_last_notification + datetime.timedelta(minutes=periodicity)

        # проверка должного датаВремени уведомления и текущего датаВремени. При совпадении - возвращаем True
        is_coincidental = notification_must_be_at.strftime("%d.%m %H:%M") == self.local_datetime.strftime("%d.%m %H:%M")

        return is_coincidental


def send_telegram_message(tg_user_id, text):
    """
    Отправляет сообщение в телеграм указанному пользователю
    :param tg_user_id: id пользователя телеграм
    :param text: тело сообщения
    :return:
    """
    params = {
        "chat_id": tg_user_id,
        "text": text,
        "parse_mode": "HTML"
    }

    response = requests.get(f'https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage', params=params)

    if response.status_code != status.HTTP_200_OK:
        print(f"Что-то пошло не так. сообщение не было отправлено. Status {response}. Параметры: {params}")


def set_new_notification_date(habit_id):
    """
    меняет время последнего уведомления на текущее время
    :param habit_id:
    :return:
    """
    habit = Habit.objects.get(pk=habit_id)
    habit.last_notification = datetime.datetime.now()
    habit.save()
