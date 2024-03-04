from datetime import timedelta

from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    PERIOD = [
        ('weekly', 'Раз в неделю'),
        ('daily', 'Каждый день'),
        ('in_one_day', 'через день')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    name = models.CharField(max_length=150, verbose_name='Название')
    action = models.TextField(verbose_name='действие привычки')
    place = models.CharField(max_length=150, verbose_name='место выполнения')
    lead_time = models.DateTimeField(verbose_name='время выполнения')
    sign_pleasant_habit = models.BooleanField(verbose_name='признак приятности привычки')
    period = models.CharField(max_length=100, choices=PERIOD, verbose_name='периодичность выполнения')
    reward = models.CharField(max_length=250, verbose_name='Вознаграждение')
    time_completed = models.DateTimeField(default=timedelta(seconds=120), verbose_name='время на выполнение')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'





