from django.contrib.auth.models import User, Permission, Group
from django.test import TestCase

from rest_framework.test import APIClient

from api.tests.test_cart import create_pizza, create_margarita, add_meal_item_in_cart

# Create your tests here.

class OrdersTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.group = Group(name = "Manager")
        self.group.save()

        self.customer1 = User.objects.create_user(
            username='customer1@customer1.com',
            password='customer1'
        )
        self.customer2 = User.objects.create_user(
            username='customer2@customer2.com',
            password='customer2'
        )
        self.manager = User.objects.create_user(
            username='manager@manager.com',
            password='manager'
        )

    def test_customers_visibility(self):
        # Customer 1
        self.user = self.customer1
        self.client.login(username='customer1@customer1.com', password='customer1')

        response = self.client.get(path="/api/orders", format="json")
        self.assertEqual(response.status_code, 200)

        # Order is empty
        orders = response.data
        self.assertEqual(0, orders['count'])

        # add pizza in Cart
        pizza = create_pizza()
        response = add_meal_item_in_cart(self.user, self.client, 1, pizza)
        self.assertEqual(response.status_code, 201)

        # add margarita in Cart
        margarita = create_margarita()
        response = add_meal_item_in_cart(self.user, self.client, 1, margarita)
        self.assertEqual(response.status_code, 201)

        # create Order for Customer 1
        response = self.client.post(path="/api/orders", format="json")
        self.assertEqual(response.status_code, 201)

        response = self.client.get(path="/api/orders", format="json")
        orders = response.data
        self.assertEqual(1, orders['count'])

        # Customer 2
        self.user = self.customer2
        self.client.login(username='customer2@customer2.com', password='customer2')

        # We don't see orders for Customer1
        response = self.client.get(path="/api/orders", format="json")
        orders = response.data
        self.assertEqual(0, orders['count'])

        # add pizza in Cart
        pizza = create_pizza()
        response = add_meal_item_in_cart(self.user, self.client, 2, pizza)
        self.assertEqual(response.status_code, 201)

        # add margarita in Cart
        margarita = create_margarita()
        response = add_meal_item_in_cart(self.user, self.client, 2, margarita)
        self.assertEqual(response.status_code, 201)

        # create Order for Customer 2
        response = self.client.post(path="/api/orders", format="json")
        self.assertEqual(response.status_code, 201)

        response = self.client.get(path="/api/orders", format="json")
        orders = response.data
        self.assertEqual(1, orders['count'])

        # Manager
        self.user = self.manager
        self.client.login(username='manager@manager.com', password='manager')

        # add Manager in manager group
        self.user.groups.add(self.group)
        self.user.save()

        # we can see both Orders from different customers
        response = self.client.get(path="/api/orders", format="json")
        self.assertEqual(response.status_code, 200)
        orders = response.data
        self.assertEqual(2, orders['count'])