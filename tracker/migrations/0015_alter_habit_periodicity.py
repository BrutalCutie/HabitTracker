# Generated by Django 5.1.4 on 2025-01-17 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0014_alter_habit_periodicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=models.IntegerField(choices=[(1440, 'Каждый день'), (2880, 'Раз в 2 дня'), (4320, 'раз в 3 дня'), (10080, 'раз в неделю')], default=1440, verbose_name='периодичность'),
        ),
    ]
