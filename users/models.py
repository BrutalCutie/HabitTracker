from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=25,
        verbose_name='псевдоним',
        null=False,
        blank=False,
        unique=True
    )

    email = models.EmailField(
        unique=True,
        verbose_name="почта"
    )

    telegram_id = models.IntegerField(
        verbose_name="Telegram ID",
        null=False,
        blank=False,
        unique=True

    )

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.pk} | {self.username}"

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
