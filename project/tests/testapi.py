from project.models import Articulo
from django.urls import reverse, resolve
from django.test import TestCase


class ArticuloTests(TestCase):
    def test_create_articulo(self):
        data = {'title': 'abc', 'content': 'sdf'}
        response = self.client.post('/api/project', data)

        self.assertEqual(response.status_code, 301)