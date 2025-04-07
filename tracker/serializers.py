from rest_framework import serializers

from tracker.models import Habit
from tracker.validators import OnlyOnePosibleValidator, NotSoLongValidator, ChainedHabitRightStateValidator, \
    NiceHabitOwnRewardValidator, HabitRightTime, HabitRightTimeToComplete, HabitRightPlace


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            OnlyOnePosibleValidator(["reward", "chained_habit"]),  # что-то одно. Или награда, или приятная привычка
            NotSoLongValidator(),  # длительность привычки не более 120сек
            ChainedHabitRightStateValidator(),  # приятная привычка должна иметь True в признаке пр-ой привычки
            NiceHabitOwnRewardValidator(),  # у приятной привычки нет своей привычки или награды
            HabitRightTime(),  # у полезной привычки должно быть время(time)
            HabitRightTimeToComplete(),  # у полезной привычки должно быть время на выполнение(time_to_complete)
            HabitRightPlace(),  # у полезной привычки должно быть место выполнения

        ]
