# models.py in lemon app
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Booking(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    guest_count = models.PositiveIntegerField(default=2, validators=[MinValueValidator(1), MaxValueValidator(10)])
    now = timezone.now().strftime("%Y-%m-%d") # default date
    reservation_time = models.DateField(default=now, editable=True)
    comments = models.CharField(max_length = 1000)

    # also show it in admin panel
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.reservation_time}"

class Cuisine(models.Model):
    name = models.CharField(max_length = 100)

    # also show it in admin panel
    def __str__(self):
        return f"{self.name}"

class Meal(models.Model):
    name = models.CharField(max_length = 100)
    cuisine = models.ForeignKey(Cuisine, on_delete = models.PROTECT)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)

    # also show it in admin panel
    def __str__(self):
        return f"{self.name} - {self.price}"
