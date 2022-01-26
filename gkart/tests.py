from django.test import TestCase
from api.category.models import Category


class APITestCase(TestCase):
    def test_auth_api(self):
        response = self.client.get('/api/auth_api/')
        self.assertEqual(response.status_code, 200)


class ModelsTestCase(TestCase):
    def test_category_model(self):
        """Posts are given slugs correctly when saving"""
        cate = Category.objects.create(category_name="Test")
        cate.save()
        self.assertEqual(cate.category_name, 'Test')