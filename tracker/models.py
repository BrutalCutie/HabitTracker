from django.db import models
from users.models import User


class Habit(models.Model):
    TO_ALL_VISIBLE_CHOICES = (
        (False, 'Видна мне'),
        (True, 'Видна всем'),
    )

    PERIODICITY_CHOISES = (
        (1440, 'Каждый день'),
        (2880, 'Раз в 2 дня'),
        (4320, 'раз в 3 дня'),
        (10080, 'раз в неделю'),
    )

    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='habits',
        verbose_name="создатель привычки",
        null=True,
        blank=True

    )
    place = models.CharField(
        max_length=50,
        verbose_name='место привычки',
        blank=True,
        null=True

    )
    time = models.TimeField(
        verbose_name="время для привычки",
        null=True,
        blank=True

    )
    action = models.CharField(
        max_length=200,
        verbose_name="действие",

    )
    is_nice_habit = models.BooleanField(
        default=False,
        verbose_name='признак приятной привычки',
    )
    chained_habit = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        related_name='nice_habbits',
        verbose_name="приятная привычка",
        blank=True,
        null=True

    )
    periodicity = models.CharField(
        max_length=30,
        choices=PERIODICITY_CHOISES,
        verbose_name='периодичность',
        default='every_day'

    )
    reward = models.CharField(
        max_length=100,
        verbose_name="вознаграждение",
        help_text="То, что вы получите за выполнение привычки",
        blank=True,
        null=True

    )
    time_to_complete = models.DurationField(
        help_text="в секундах(до 120 сек)",
        verbose_name="длительность выполнения привычки",
        null=True,
        blank=True

    )
    publish_to_all = models.BooleanField(
        choices=TO_ALL_VISIBLE_CHOICES,
        verbose_name="признак публичности",
        help_text="привычка будет видна всем или только вам",

    )

    last_notification = models.DateTimeField(
        verbose_name="дата последнего уведомления",
        default=None,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.pk} | {self.action}"

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
