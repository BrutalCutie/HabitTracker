from rest_framework import viewsets, generics

from tracker.models import Habit
from tracker.paginators import HabitsPagination
from tracker.permissions import IsHabitOwner
from tracker.serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitsPagination

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()

        if not habit.is_nice_habit:  # если это полезная привычка - запускаем отложенную задачу напоминания
            periodicity_time = habit.periodicity

            # send_notification.delay(habit.pk)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'delete']:
            self.permission_classes = [IsHabitOwner]

        return super().get_permissions()

    def get_queryset(self): return Habit.objects.filter(owner=self.request.user.pk)


class PublishedHabitsListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(publish_to_all=True)
    pagination_class = HabitsPagination


class PublishedHabitsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(publish_to_all=True)
