# Generated by Django 5.1.4 on 2024-12-20 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0011_habit_last_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='last_notification',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='последнее уведомление'),
        ),
    ]