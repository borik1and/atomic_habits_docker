from django.conf import settings
from datetime import timedelta
import requests


class TelegramBotService:
    URL = settings.TELEGRAM_BOT_URL
    TOKEN = settings.TELEGRAM_BOT_TOKEN

    def send_message(self, text):
        response = requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': '1115606350',
                'text': text
            }
        )


