from django.contrib import admin

from .models import (
    Cart, Category, Cuisine, Meal, Order, OrderItem,
)

# Register your models here.

admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Cuisine)
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(OrderItem)