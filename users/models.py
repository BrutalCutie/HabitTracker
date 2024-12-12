from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=25,
        verbose_name='псевдоним',
        null=False,
        blank=False,
    )
    telegram_id = models.IntegerField(
        max_length=20,
        verbose_name="Telegram ID",
        null=False,
        blank=False,

    )

    def __str__(self):
        return f"{self.pk} | {self.username}"

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
