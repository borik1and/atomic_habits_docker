from django.core.management import BaseCommand

from users.services import TelegramBotService


class Command(BaseCommand):
    def handle(self, *args, **options):
        my_bot = TelegramBotService()
        my_bot.send_message('Hi<This id your bot speaking>')
