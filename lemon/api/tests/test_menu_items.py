from django.contrib.auth.models import User, Permission, Group
from django.test import TestCase

from rest_framework.test import APIClient

from api.models import Category, Cuisine

# Create your tests here.

class CartTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.group = Group(name = "Manager")
        self.group.save()

        self.user = User.objects.create_user(
            username='manager@manager.com',
            password='manager'
        )

    # user without a group
    def test_menu_items_no_auth(self):
        self.client.login(username='manager@manager.com', password='manager')

        response = self.client.get(path="/api/menu-items", format="json")
        self.assertEqual(response.status_code, 200)

        cart = response.data
        self.assertEqual(0, cart['count'])

        # create Category
        category = Category.objects.create(
            title = "Main"
        )
        # create Cuisine
        cuisine = Cuisine.objects.create(
            name = "Italian"
        )
        # Meal
        data = {
            "name" : "Pizza",
            "cuisine.name" : cuisine.id,
            "category.title" : category.id,
            "price" : 10.00,
            "desc" : 'Original pizza',
            "image" : '/static/path_to_image/pizza.jpg',
            "image_text" : 'Pizza'
        }
        # post
        response = self.client.post(
            path = "/api/menu-items",
            data = data,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 403)
        # put
        response = self.client.post(
            path = "/api/menu-items",
            data = data,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 403)
        # patch
        response = self.client.patch(
            path = "/api/menu-items",
            data = data,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 403)
        # delete
        response = self.client.delete(
            path = "/api/menu-items",
            format = "json"
        )
        self.assertEqual(response.status_code, 403)

    # user in manager group
    def test_menu_items_add_new_item(self):
        # add user to group
        self.user.groups.add(self.group)
        self.user.save()

        self.client.login(username='manager@manager.com', password='manager')

        response = self.client.get(path="/api/menu-items", format="json")
        self.assertEqual(response.status_code, 200)

        cart = response.data
        self.assertEqual(0, cart['count'])

        # create Category
        category = Category.objects.create(
            title = "Main"
        )
        # create Cuisine
        cuisine = Cuisine.objects.create(
            name = "Italian"
        )
        # Meal
        data = {
            "name" : "Pizza",
            "cuisine" : {"name" : cuisine.name},
            "category" : {"title" : category.title},
            "price" : '10.00',
            "desc" : 'Original pizza',
            "image" : '/static/path_to_image/pizza.jpg',
            "image_text" : 'Pizza'
        }
        # create new menu-item
        response = self.client.post(
            path = "/api/menu-items",
            data = data,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 201)

        # get again
        response = self.client.get(path="/api/menu-items", format="json")
        self.assertEqual(response.status_code, 200)

        cart = response.data
        self.assertEqual(1, cart['count'])
