from django.core.management import BaseCommand

from habit.services import TelegramBotService


class Command(BaseCommand):
    def handle(self, *args, **options):
        my_bot = TelegramBotService()
        my_bot.send_message('1115606350', 'Hi<This id your bot speaking>')
