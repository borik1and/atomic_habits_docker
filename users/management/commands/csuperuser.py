from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            username="admin",
            email='admin@edu.com',
            first_name='admin',
            last_name='root',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password('1975')
        user.save()

        self.stdout.write(self.style.SUCCESS('Суперпользователь успешно создан.'))
