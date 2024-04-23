from rest_framework import serializers

from .models import Meal

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'name', 'cuisine', 'price', 'desc', 'image', 'image_text']
        # name = serializers.CharField(max_length = 100)
        # cuisine = serializers.CharField(max_length = 100)
        # price = serializers.DecimalField(max_digits = 5, decimal_places = 2)
        # desc = serializers.CharField(max_length=1000)
        # image = serializers.CharField(max_length=200)
        # image_text = serializers.CharField(max_length=200)