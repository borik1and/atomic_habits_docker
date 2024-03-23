from datetime import timedelta, datetime
from celery import shared_task
from celery.utils.time import timezone

from habit.services import TelegramBotService
from habit.models import Habit
from users.models import User


@shared_task
def send_message():
    users = User.objects.get()
    # habits = Habit.objects.all()
    # for habit in habits:
    for user in users:
        bot = TelegramBotService()
        bot.send_message(user.chat_id, 'test message')


@shared_task
def check_messages_sending():
    habits = Habit.objects.filter()
    current_time = timezone.now()
    for habit in habits:
        if habit.next_dispatch_time is None or habit.next_dispatch_time == current_time:
            telegram_bot = TelegramBotService()
            telegram_bot.send_message(habit.user.chat_id, f'Напоминание привычки {habit.name}сделать в '
                                                          f'{habit.place}вот это:{habit.action},'
                                                          f' а потом наградить себя {habit.reward}')
            # Проверка, если next_dispatch_time не установлен, либо если оно равно текущему времени
            if habit.next_dispatch_time is None or habit.next_dispatch_time == current_time:
                habit.next_dispatch_time = current_time + timedelta(days=habit.period)
            else:
                habit.next_dispatch_time = habit.next_dispatch_time + timedelta(days=habit.period)
            habit.save()
