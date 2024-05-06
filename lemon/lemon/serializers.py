from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import Cart, Cuisine, Meal, Order, OrderItem

# Allows to display the name of cuisine for Meal
class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ['name']

class MealSerializer(serializers.ModelSerializer):
    # Could add a hyperlink instead of int id
    id = serializers.HyperlinkedRelatedField(many=False, view_name='menu-item-view', read_only=True)
    cuisine = CuisineSerializer()
    class Meta:
        model = Meal
        fields = '__all__'

    def create(self, validated_data):
        cuisine_data = validated_data.pop('cuisine')
        # find cuisine object by name
        cuisine = Cuisine.objects.get(name = cuisine_data['name'])
        # add cuisine
        validated_data["cuisine"] = cuisine
        # create new meal object in DB
        meal = Meal.objects.create(**validated_data)
        return meal

    def update(self, instance, validated_data):
        cuisine_data = validated_data.pop('cuisine')
        # find cuisine object by name
        cuisine = Cuisine.objects.get(name = cuisine_data['name'])

        instance.name = validated_data.get('name', instance.name)
        instance.cuisine = cuisine
        instance.price = validated_data.get('price', instance.price)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.image = validated_data.get('image', instance.image)
        instance.image_text = validated_data.get('image_text', instance.image_text)
        instance.save()

        return instance

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [User._meta.pk.name, User.USERNAME_FIELD, 'first_name', 'last_name', 'email', 'is_active']

class CartSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    meal_id = serializers.IntegerField()
    class Meta:
        model = Cart
        fields = ['user_id', 'meal_id', 'count']

class OrderSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedRelatedField(many=False, view_name='order-item-view', read_only=True)
    customer_id = serializers.IntegerField()
    delivery_id = serializers.IntegerField()
    status = serializers.CharField()

    class Meta:
        model = Order
        fields = ['id', 'customer_id', 'delivery_id', 'status']

class OrderItemSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField()
    meal_id = serializers.IntegerField()
    count = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ['order_id', 'meal_id', 'count']
