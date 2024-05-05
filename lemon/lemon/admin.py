from django.contrib import admin

from .models import Booking
from .models import Cart
from .models import Cuisine
from .models import Meal

# Register your models here.

admin.site.register(Booking)
admin.site.register(Cart)
admin.site.register(Cuisine)
admin.site.register(Meal)