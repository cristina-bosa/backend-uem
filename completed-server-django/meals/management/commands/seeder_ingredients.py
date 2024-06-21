from django.core.management import BaseCommand


class SeederIngredientsCommand(BaseCommand):
    help = "Ingredients seeder"

    INGREDIENTS_DATA = [
        'Aceite de oliva','Ajo','Albahaca','Arroz','Azúcar','Berenjena','Brócoli','Cebolla','Champiñones','Chocolate',
        'Cilantro','Comino','Harina de trigo','Huevos','Leche','Lentejas','Limón','Mantequilla','Manzana','Miel','Orégano',
        'Papas','Pasta','Pepino','Perejil','Pimiento rojo','Pollo','Queso','Sal','Salmón','Tomate','Vainilla','Vinagre','Yogur',
        'Zanahoria'
        ]

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('Seeder ingredients - Started')
        self.__create_ingredients()
        print('Seeder ingredients - Finished')

    def __create_ingredients(self):
        print('Seeder ingredients - Creating ingredients')
        from meals.models.ingredients import Ingredients
        list_ingredients = []
        for ingredient in self.INGREDIENTS_DATA:
            try:
                list_ingredients.append(Ingredients.objects.create(
                    name = ingredient
                ))
            except Exception as e:
                print(f'{ingredient} already exists')
