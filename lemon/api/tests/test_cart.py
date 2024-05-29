from django.contrib.auth.models import User
from django.test import TestCase

from rest_framework.test import APIClient

from api.models import Category, Cuisine, Meal

# Create your tests here.

class CartTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username='admin@admin.com',
            password='admin'
        )

    def test_cart_no_auth(self):
        response = self.client.get(path="/api/cart/menu-items", format="json")
        self.assertEqual(response.status_code, 401)

    def test_cart_post_get_delete_with_auth(self):
        self.client.login(username='admin@admin.com', password='admin')

        response = self.client.get(path="/api/cart/menu-items", format="json")
        self.assertEqual(response.status_code, 200)

        # Cart is empty
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
        # create Meal
        pizza = Meal.objects.create(
            name = "Pizza",
            cuisine = cuisine,
            category = category,
            price = 10.00,
            desc = 'Original pizza',
            image = '/static/path_to_image/pizza.jpg',
            image_text = 'Pizza'
        )

        # create Cart
        data = {
            "user_id" : self.user.id,
            "meal_id" : pizza.id,
            "count" : 2,
            "unit_price" : 10.00,
            "price" : 20.00,
        }
        response = self.client.post(
            path = "/api/cart/menu-items",
            data = data,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 201)

        # Cart is NOT empty
        response = self.client.get(path="/api/cart/menu-items", format="json")
        self.assertEqual(response.status_code, 200)
        cart = response.data
        self.assertEqual(1, cart['count'])

        response = self.client.delete(path="/api/cart/menu-items")
        self.assertEqual(response.status_code, 204) # deleted

        response = self.client.delete(path="/api/cart/menu-items")
        self.assertEqual(response.status_code, 204) # deleted

        # Cart is empty again
        response = self.client.get(path="/api/cart/menu-items", format="json")
        self.assertEqual(response.status_code, 200)
        cart = response.data
        self.assertEqual(0, cart['count'])
