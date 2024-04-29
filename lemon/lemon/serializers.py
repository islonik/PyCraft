from rest_framework import serializers

from .models import Cuisine
from .models import Meal

# Allows to display the name of cuisine for Meal
class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ['name']

class MealSerializer(serializers.HyperlinkedModelSerializer):
    # Could add a hyperlink instead of int id
    #id = serializers.HyperlinkedRelatedField(many=False, view_name='menu-item-view', read_only=True)
    cuisine = serializers.StringRelatedField()
    class Meta:
        model = Meal
        fields = ['id', 'name', 'cuisine', 'price', 'desc', 'image', 'image_text']