from habit.services import TelegramBotService
from habit.models import Habit
from celery import shared_task
from datetime import datetime, timedelta


@shared_task
def send_message():
    habits = Habit.objects.filter()
    current_time = datetime.now()
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
