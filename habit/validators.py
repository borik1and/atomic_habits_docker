from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_reward_and_related_habit(reward, related_habit):
    if bool(reward) == bool(related_habit):
        raise ValidationError(_('Должно быть заполнено либо поле "Вознаграждение", либо поле "Связанная привычка".'))


def validate_time_to_complete(value):
    if value.total_seconds() > 120:
        raise ValidationError(_('Время на выполнение привычки не должно превышать 2 минут.'))
