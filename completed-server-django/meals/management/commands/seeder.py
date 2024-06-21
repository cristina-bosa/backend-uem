from django.core.management import BaseCommand

from .seeder_categories import SeederCategoriesCommand
from .seeder_ingredients import SeederIngredientsCommand
from .seeder_users import SeederUsersCommand


class Command(BaseCommand):
    help = "Seeder"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('Seeder - Started 🚀')
        SeederUsersCommand().handle()
        SeederCategoriesCommand().handle()
        SeederIngredientsCommand().handle()
        print('Seeder - Finished 🎉')
