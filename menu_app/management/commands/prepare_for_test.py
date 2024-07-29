from django.core.management import BaseCommand, call_command


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('\nThe project configure begins . . .\n')

        print('manage.py migrate . . .\n')
        call_command('migrate')
        print('Success!\n')

        print('manage.py load data data.json . . .\n')
        call_command('loaddata', 'data.json')
        print("""admin data
username: admin
password: admin""")
        print('Success!\n')

        print('manage.py runserver . . .')
        call_command('runserver')
