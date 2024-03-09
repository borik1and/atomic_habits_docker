from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    name = models.CharField(max_length=150, verbose_name='Название')
    action = models.TextField(verbose_name='Действие привычки')
    place = models.CharField(max_length=150, verbose_name='Место выполнения')
    lead_time = models.DateTimeField(verbose_name='Время выполнения')
    sign_pleasant_habit = models.BooleanField(default=False, verbose_name='Признак приятности привычки')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,
                                      verbose_name='Связанная привычка')
    period = models.IntegerField(default=1, verbose_name='Периодичность выполнения')
    reward = models.CharField(max_length=250, blank=True, verbose_name='Вознаграждение')
    time_to_complete = models.DurationField(default='00:02:00', verbose_name='Время на выполнение')
    telegram_id = models.CharField(max_length=50, verbose_name='телеграм ID', **NULLABLE)

    def clean(self):
        if self.related_habit and not self.related_habit.sign_pleasant_habit:
            raise ValidationError('Связанная привычка должна быть приятной.')

        if 1 >= self.period >= 7:
            raise ValidationError('Нельзя устанавливать привычку реже, менее 1 и более 7')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
