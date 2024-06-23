from django.core.management import BaseCommand

from .seeder_categories import SeederCategoriesCommand
from .seeder_ingredients import SeederIngredientsCommand
from .seeder_recipes import SeederRecipesCommand
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
        SeederRecipesCommand().handle()
        print('Seeder - Finished 🎉')
