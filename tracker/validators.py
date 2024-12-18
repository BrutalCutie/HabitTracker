from datetime import timedelta

from rest_framework.exceptions import ValidationError


class OnlyOnePosibleValidator:
    def __init__(self, fields: list):
        self.fields = fields

    def __call__(self, data):
        one_posible = False
        for field in self.fields:
            result = dict(data).get(field)

            if result and not one_posible:
                one_posible = True
                continue

            elif not result:
                continue

            raise ValidationError(f"Из полей {', '.join(self.fields)} выбрать можно только одно.")


class NotSoLongValidator:
    def __call__(self, data):
        time_to_complete: timedelta = dict(data).get('time_to_complete', timedelta(seconds=0))
        if time_to_complete.seconds > 120:
            raise ValidationError("Время выполнения не может быть более 120 секунд")


class ChainedHabitRightStateValidator:
    def __call__(self, data):
        chained_habit = data.get('chained_habit')
        if chained_habit:
            if not chained_habit.is_nice_habit:
                err_text = "При выборе приятной привычки - признак приятной привычки(is_nice_habit) должем быть True"
                raise ValidationError(err_text)


class NiceHabitOwnRewardValidator:

    def __call__(self, data):
        is_nice_habit = data.get('is_nice_habit')
        chained_habit = data.get("chained_habit")
        habit_reward = data.get('reward')

        if any([chained_habit, habit_reward]) and is_nice_habit:
            raise ValidationError("Приятная привычка не может содержать свою привычку или награду за выполнение")


class HabitRightTime:
    def __call__(self, data):
        is_nice_habit = data.get('is_nice_habit')

        if is_nice_habit:
            return

        if not data.get('time'):
            raise ValidationError("Полезная привычка должна содержать время для выполнения(\"time\")")


class HabitRightTimeToComplete:
    def __call__(self, data):
        is_nice_habit = data.get('is_nice_habit')

        if is_nice_habit:
            return

        if not data.get('time_to_complete'):
            raise ValidationError("Полезная привычка должна содержать длительность выполнения(\"time_to_complete\")")


class HabitRightPlace:
    def __call__(self, data):
        is_nice_habit = data.get('is_nice_habit')

        if is_nice_habit:
            return

        if not data.get('place'):
            raise ValidationError("Полезная привычка должна содержать место выполнения(\"place\")")

