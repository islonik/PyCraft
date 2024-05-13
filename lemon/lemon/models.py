# models.py in lemon app
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Booking(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    guest_count = models.PositiveIntegerField(default=2, validators=[MinValueValidator(1), MaxValueValidator(10)])
    reservation_time = models.DateField()
    comments = models.CharField(max_length = 1000)

    # also show it in admin panel
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.reservation_time}"
