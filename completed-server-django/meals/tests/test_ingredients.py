from rest_framework import status
from rest_framework.test import APITestCase
from authentication.models import Users
from meals.models.ingredients import Ingredients


class IngredientCreateTestCase(APITestCase):
    def setUp(self):
        print('Ingredient testing...')
        self.user = Users.objects.create_superuser(username='test', password = 'test')
        self.client.force_authenticate(user = self.user)
        self.data = {'id': 1, 'name': 'Chocolate'}
        self.ingredient = Ingredients(**self.data)
        self.ingredient.save()
    def test_ingredient_creation(self):
        data = { 'id': 2, 'name': 'Queso'}
        response = self.client.post('/api/ingredients/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_ingredient_get(self):
        response = self.client.get(f'/api/ingredients/{self.data['id']}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_update_ingredient(self):
        data = {'name': 'Cacao'}
        response = self.client.put(f'/api/ingredients/{self.ingredient.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_delete_ingredient(self):
        response = self.client.delete(f'/api/ingredients/{self.ingredient.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Ingredients.objects.filter(id=self.ingredient.id).exists())