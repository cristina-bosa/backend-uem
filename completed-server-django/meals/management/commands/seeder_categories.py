from django.core.management import BaseCommand


class SeederCategoriesCommand(BaseCommand):
    help = "Categories seeder"

    CATEGORIES_DATA = [
        'Desayuno',
        'Almuerzo',
        'Cena',
        'Aperitivo',
        'Postre',
        'Ensaladas',
        'Sopas',
        'Bebidas',
        'Entrantes',
        'Platos principales',
        'Guarniciones',
        'Salsas y aderezos',
        'Panadería',
        'Pastelería',
        'Mariscos',
        'Carnes',
        'Vegetariano',
        'Vegano',
        'Sin gluten',
        'Dieta keto',
        'Comida rápida',
        'Comida saludable',
        'Internacional',
        'Comida mexicana',
        'Comida italiana',
        'Comida china',
        'Comida japonesa',
        'Comida india',
        'Comida mediterránea'
        ]

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('Seeder categories - Started')
        self.__create_categories()
        print('Seeder categories - Finished')

    def __create_categories(self):
        print('Seeder categories - Creating categories')
        from meals.models.categories import Categories
        list_categories = []
        for category in self.CATEGORIES_DATA:
            try:
                list_categories.append(Categories.objects.create(
                    name = category
                ))
            except Exception as e:
                print(f'{category} already exists')