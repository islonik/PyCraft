from django.contrib.auth.models import User
from django.test import TestCase

from rest_framework.test import APIClient

from api.models import Booking

# Create your tests here.

class BookingTestCase(TestCase):

    def create_bookings(self):
        booking1 = Booking.objects.create(
            first_name = "Miya",
            last_name = "Kazuki",
            guest_count = 2,
            reservation_date = "2024-05-23",
            reservation_time="5 PM",
            comments = "My regular meal."
        )
        booking2 = Booking.objects.create(
            first_name = "Mato",
            last_name = "Sato",
            guest_count = 2,
            reservation_date = "2024-05-24",
            reservation_time="6 PM",
            comments = "My fancy meal."
        )
        booking3 = Booking.objects.create(
            first_name = "David",
            last_name = "Weber",
            guest_count = 3,
            reservation_date = "2024-05-25",
            reservation_time="7 PM",
            comments = "My family meal."
        )
        # return list with the created bookings
        return [booking1, booking2, booking3]

    def setUp(self):
        self.expected_bookings = self.create_bookings()
        self.client = APIClient()

        self.user = User.objects.create_user(
            username='admin@admin.com',
            password='admin'
        )

    def test_bookings_get_no_auth(self):
        response = self.client.get(path="/api/bookings", format="json")
        self.assertEqual(response.status_code, 401)

    def test_bookings_get_with_auth(self):
        self.client.login(username='admin@admin.com', password='admin')

        response = self.client.get(path="/api/bookings", format="json")
        self.assertEqual(response.status_code, 200)

        bookings = response.data
        self.assertEqual(len(self.expected_bookings), bookings['count'])
        self.assertEqual(len(self.expected_bookings), len(bookings['results']))
        self.assertEqual('Miya', bookings['results'][0]['first_name'])
        self.assertEqual('Mato', bookings['results'][1]['first_name'])
        self.assertEqual('David', bookings['results'][2]['first_name'])
