from rest_framework import status
from rest_framework.test import APITestCase
from authentication.models import Users
from meals.models.categories import Categories

class CategoryTestCase(APITestCase):
    def setUp(self):
        print('Categories testing...')
        self.user = Users.objects.create_superuser(username='test', password='test')
        self.client.force_authenticate(user=self.user)
        self.data = {'id': 1, 'name': 'Desayuno'}
        self.category = Categories(**self.data)
        self.category.save()

    def test_category_creation(self):
        data = {'id': 2, 'name': 'Almuerzo'}
        response = self.client.post('/api/categories/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Almuerzo')

    def test_category_get(self):
        response = self.client.get(f'/api/categories/{self.data["id"]}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Desayuno')

    def test_update_category(self):
        data = {'name': 'Cena'}
        response = self.client.put(f'/api/categories/{self.category.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Cena')

    def test_delete_category(self):
        response = self.client.delete(f'/api/categories/{self.category.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Categories.objects.filter(id=self.category.id).exists())
