from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Item, Tag

class ItemTests(APITestCase):
    def test_view_items(self):
        url = reverse('item-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
