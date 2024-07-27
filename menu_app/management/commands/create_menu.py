from django.core.management import BaseCommand
from django.db import IntegrityError
from menu_app.models import Menu


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            menu = Menu.objects.create(name='main_menu')
            menu.save()
        except IntegrityError:
            print('Menu main_menu already exists')
