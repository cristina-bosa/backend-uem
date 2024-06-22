from rest_framework import status
from rest_framework.test import APITestCase
from authentication.models import Users
from meals.models.categories import Categories
from meals.models.ingredients import Ingredients
from meals.models.recipes import Recipes


class RecipesTestCase(APITestCase):
    def setUp(self):
        print('Recipes testing...')
        self.user = Users.objects.create_superuser(username = 'test', password = 'test')
        self.client.force_authenticate(user = self.user)

        self.category = Categories(name = 'Desayuno')
        self.category.save()

        self.ingredient = Ingredients(name = 'Pan')
        self.ingredient.save()

        self.recipe_data = {
            'name': 'Tostadas',
            'instructions': 'Tuesta el pan y ponle mantequilla.',
            'time': '00:10:00',
            'difficulty': 1,
            'owner_id': self.user.id,
            'category_id': self.category.id
            }
        self.recipe = Recipes(**self.recipe_data)
        self.recipe.save()



    def test_recipe_creation(self):
        data = {
            "name": "Gyozas",
            "instructions": "Instrucciones de como preparar unas ricas y jugosas gyozas",
            "time": "01:00",
            "difficulty": 6,
            "owner": self.user.id,
            "category": self.category.id
            }
        response = self.client.post('/api/recipes/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_recipe_get(self):
        response = self.client.get(f'/api/recipes/{self.recipe.id}/', format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Tostadas')
    #
    def test_update_recipe(self):
        data = {
            'name': 'Tostadas con mantequilla',
            'instructions': 'Tuesta el pan, ponle mantequilla y un poco de miel.',
            'time': '00:15:00',
            'difficulty': 1,
            'owner': self.user.id,
            'category': self.category.id
            }
        response = self.client.put(f'/api/recipes/{self.recipe.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_ingredient_to_recipe(self):
        data = {
            "ingredients": [{'ingredient': self.ingredient.id, 'quantity': 2}]
            }
        response = self.client.post(f'/api/recipes/{self.recipe.id}/add-ingredients/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_ingredient_from_recipe(self):
        data = {
            "ingredients": [
                self.ingredient.id
                ]
            }
        response = self.client.post(f'/api/recipes/{self.recipe.id}/delete-ingredients/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_recipe(self):
        response = self.client.delete(f'/api/recipes/{self.recipe.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Recipes.objects.filter(id = self.recipe.id).exists())

    def test_my_recipes(self):
        response = self.client.get('/api/recipes/me/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
