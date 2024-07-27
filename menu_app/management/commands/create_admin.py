from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import IntegrityError


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            admin = User.objects.create(
                username="admin",
                is_superuser=True,
                is_staff=True,
                is_active=True
            )

            admin.set_password('admin')
            admin.save()
        except IntegrityError:
            print('Superuser already exists.')
        finally:
            print(f'Username: admin, password: admin')
