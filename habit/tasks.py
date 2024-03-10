from datetime import timedelta, datetime
from celery import shared_task
from habit.services import TelegramBotService
from habit.models import Habit


@shared_task
def check_messages_sending(pk):
    habits = Habit.objects.filter(pk=pk)
    for habit in habits:
        if habit.next_dispatch_time is None or habit.next_dispatch_time == datetime.now():
            telegram_bot = TelegramBotService()
            telegram_bot.send_message(habit.chat_id, f'Напоминание привычки {habit.name}')
            if habit.next_dispatch_time is None:
                habit.next_dispatch_time = datetime.now() + timedelta(days=habit.period)
            else:
                habit.next_dispatch_time = habit.next_dispatch_time + timedelta(days=habit.period)
    Habit.objects.bulk_update(habits, ['next_dispatch_time'])
