from django.db import models
from users.models import User


class Habit(models.Model):
    TO_ALL_VISIBLE_CHOICES = (
        (False, 'Видна мне'),
        (True, 'Видна всем'),
    )

    PERIODICITY_CHOISES = (
        ("every_day", 'Каждый день'),
        ("once_2day", 'Раз в 2 дня'),
        ("once_3day", 'раз в 3 дня'),
    )

    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='habits',
        verbose_name="создатель привычки",

    )
    place = models.CharField(
        max_length=50,
        verbose_name='место привычки',

    )
    time = models.DateTimeField(
        verbose_name="время для привычки",

    )
    action = models.CharField(
        max_length=200,
        verbose_name="действие",

    )
    is_nice_habbit = models.BooleanField(
        default=False,
        verbose_name='признак приятной привычки',
    )
    chained_habit = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        related_name='nice_habbits',
        verbose_name="приятная привычка",

    )
    periodicity = models.CharField(
        choices=PERIODICITY_CHOISES,
        verbose_name='периодичность',

    )
    reward = models.CharField(
        max_length=100,
        verbose_name="вознаграждение",
        help_text="То, что вы получите за выполнение привычки",

    )
    time_to_complete = models.DurationField(
        help_text="в секундах(до 120 сек)",
        verbose_name="длительность выполнения привычки",

    )
    publish_to_all = models.BooleanField(
        choices=TO_ALL_VISIBLE_CHOICES,
        verbose_name="признак публичности",
        help_text="привычка будет видна всем или только вам",

    )

    def __str__(self):
        return f"{self.pk} | {self.owner.username}"

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
