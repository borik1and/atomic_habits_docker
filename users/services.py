from django.conf import settings
import requests


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
