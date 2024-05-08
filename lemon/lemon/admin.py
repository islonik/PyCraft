from django.contrib import admin

from .models import Booking
from .models import Cart
from .models import Category
from .models import Cuisine
from .models import Meal
from .models import Order
from .models import OrderItem

# Register your models here.

admin.site.register(Booking)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Cuisine)
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(OrderItem)