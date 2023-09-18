from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient

class MenuItemTest(TestCase):
    def setUp(self):
        self.menu_item1 = Menu.objects.create(title="Item 1", price=10, inventory=100)
        self.menu_item2 = Menu.objects.create(title="Item 2", price=15, inventory=50)
        self.menu_item3 = Menu.objects.create(title="Item 3", price=20, inventory=75)
    def test_get_all(self):
        url = reverse('menu-list')
        client = APIClient()
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serialized_data = MenuSerializer([self.menu_item1, self.menu_item2, self.menu_item3], many=True)

        self.assertEqual(response.data, serialized_data.data)