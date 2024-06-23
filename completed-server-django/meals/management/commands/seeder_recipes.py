from django.core.management import BaseCommand


class SeederRecipesCommand(BaseCommand):
    help = "Recipes seeder"

    RECIPES_DATA=[
        {
            'name': 'Gyozas',
             'instructions': '1. En un bol, mezcla la carne de cerdo, el ajo, el jengibre, la cebolla, la salsa de soja y el aceite de sésamo. 2. Coloca una cucharadita de relleno en el centro de cada disco de masa. 3. Humedece los bordes de la masa con agua y dobla la masa por la mitad. 4. Presiona los bordes para sellar. 5. Calienta aceite en una sartén y coloca las gyozas. 6. Agrega agua y tapa la sartén. 7. Cocina hasta que el agua se evapore y las gyozas estén doradas. 8. Sirve con salsa de soja y aceite de sésamo.',
             'time': '00:30:00',
             'difficulty': 7,
             'owner_id': 1,
             'category_id': 4
         },
        {
            'name': 'Tarta de manzana',
            'instructions': '1. Precalienta el horno a 180°C. 2. En un bol, mezcla la harina, la manteca, el azúcar y el huevo. 3. Estira la masa y colócala en un molde. 4. Pela las manzanas y córtalas en rodajas. 5. Coloca las manzanas sobre la masa. 6. Espolvorea con azúcar y canela. 7. Hornea durante 30 minutos. 8. Sirve caliente con helado de vainilla.',
            'time': '01:00:00',
            'difficulty': 5,
            'owner_id': 2,
            'category_id': 5
        },
    ]
    INGREDIENTS_DATA=[
        {"recipe_name": 'Gyozas', "ingredient_id": 1, "quantity": 400},
        {"recipe_name": 'Gyozas', "ingredient_id": 2, "quantity": 2},
        {"recipe_name": 'Gyozas', "ingredient_id": 4, "quantity": 2},
        { "recipe_name": 'Tarta de manzana', "ingredient_id": 1, "quantity": 400 },
        { "recipe_name": 'Tarta de manzana', "ingredient_id": 2, "quantity": 2 },
        { "recipe_name": 'Tarta de manzana', "ingredient_id": 4, "quantity": 2 },
    ]

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('Seeder recipes - Started')
        self.__create_recipes()
        print('Seeder recipes - Finished')

    def __create_recipes(self):
        print ('Seeder recipes - Creating recipes 🍳')
        from meals.models.recipes import Recipes
        for recipe in self.RECIPES_DATA:
            try:
                Recipes.objects.create(
                    name = recipe['name'],
                    instructions = recipe['instructions'],
                    time = recipe['time'],
                    difficulty = recipe['difficulty'],
                    owner_id = recipe['owner_id'],
                    category_id = recipe['category_id']
                )
                print(f'{recipe["name"]} created')
            except Exception as e:
                raise e
        print('\n')
        for ingredient in self.INGREDIENTS_DATA:
            recipe = Recipes.objects.get(name=ingredient['recipe_name'])
            recipe.recipesingredients_set.create(
                ingredient_id = ingredient['ingredient_id'],
                quantity = ingredient['quantity']
            )



