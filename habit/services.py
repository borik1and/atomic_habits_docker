from django.conf import settings
import requests
import json
from datetime import datetime, timedelta
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django_celery_beat.models import PeriodicTask


class TelegramBotService:
    URL = settings.TELEGRAM_BOT_URL
    TOKEN = settings.TELEGRAM_BOT_TOKEN

    def send_message(self, chat_id, text):
        response = requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': chat_id,
                'text': text
            }
        )
        return response


def set_schedule(*args, **kwargs):
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=10,
        period=IntervalSchedule.MINUTES,
    )
    PeriodicTask.objects.create(
        interval=schedule,  # we created this above.
        name='sending bot messages',  # simply describes this periodic task.
        task='habit.tasks.check_messages_sending',  # name of task.
        args=json.dumps(['arg1', 'arg2']),
        kwargs=json.dumps({
            'be_careful': True,
        }),
        expires=datetime.utcnow() + timedelta(seconds=30)
    )
