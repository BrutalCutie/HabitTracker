from celery import shared_task

from tracker.models import Habit
from tracker.services import HabitTimeControl, send_telegram_message


@shared_task
def remind_controler():
    """
    Проверка на необходимость отослать уведомление о привычке
    :return:
    """
    all_habits = Habit.objects.filter(is_nice_habit=False)  # пул только полезных привычек
    for habit in all_habits:

        hc = HabitTimeControl(habit.time)

        if not hc.time_control():  # продолжить перебор, если есть несовпадение по времени
            continue

        # проверка на полное совпадение должной датыВремени уведомления и текущей
        if hc.is_today_notification(habit.last_notification, habit.periodicity):
            send_notification.delay(habit.pk)


@shared_task
def send_notification(habit_id):
    """

    :param habit_id:
    :return:
    """
    habit = Habit.objects.get(pk=habit_id)
    user = habit.owner

    if habit.chained_habit is not None:
        reward = habit.chained_habit.action
    else:
        reward = habit.reward

    text = (f"Привет {user.username}!\n<u>Напоминаю о твоей полезной привычке в {habit.time.strftime("%H:%M")}</u>!\n"
            f"Действие: <b>{habit.action}</b>\n"
            f"Место: {habit.place}\n"
            f"Делай на протяжении {habit.time_to_complete.seconds} сек и в награду можешь: {reward}")

    send_telegram_message(tg_user_id=user.telegram_id, text=text)
