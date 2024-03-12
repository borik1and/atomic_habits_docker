from datetime import timedelta
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    name = models.CharField(max_length=150, verbose_name='Название')
    action = models.TextField(verbose_name='Действие привычки')
    place = models.CharField(max_length=150, verbose_name='Место выполнения')
    sign_pleasant_habit = models.BooleanField(default=False, verbose_name='Признак приятности привычки')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,
                                      verbose_name='Связанная привычка')
    period = models.IntegerField(default=1, verbose_name='Периодичность выполнения')
    reward = models.CharField(max_length=250, blank=True, verbose_name='Вознаграждение')
    time_to_complete = models.DurationField(default=timedelta(minutes=2), verbose_name='Время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')
    next_dispatch_time = models.DateTimeField(default=None, **NULLABLE, verbose_name='время следующей отправки')

    def clean(self):
        if self.related_habit and not self.related_habit.sign_pleasant_habit:
            raise ValidationError(_('Связанная привычка должна быть приятной.'))

        if self.period < 1 or self.period > 7:
            raise ValidationError(_('Нельзя устанавливать привычку реже, чем 1 и более 7'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
