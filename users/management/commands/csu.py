from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Create SuperUser
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@almaz25.pro',
            name='almaz',
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )

        user.set_password('12345678')
        user.save()