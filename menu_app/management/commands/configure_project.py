from django.core.management import BaseCommand, call_command


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('\nThe project configure begins . . .\n')

        print('manage.py migrate . . .')
        call_command('migrate')
        print('Success!')

        print('manage.py create_admin . . .')
        call_command('create_admin')
        print('Success!')

        print('manage.py create_menu . . .')
        call_command('create_menu')
        print('Success!')

        print('manage.py runserver . . .')
        call_command('runserver')
