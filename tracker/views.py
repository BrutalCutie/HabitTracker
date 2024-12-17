from rest_framework import viewsets

from tracker.models import Habit
from tracker.paginators import HabitsPagination
from tracker.serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(publish_to_all=True)
    pagination_class = HabitsPagination
