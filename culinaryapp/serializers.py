from rest_framework import serializers

from culinaryapp.models import Dish, DishIngredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishIngredient
        fields = ['ingredient', 'quantity', 'quantity_description']

class DishSerializer(serializers.ModelSerializer):
    dish_ingredients = IngredientSerializer(many=True)
    class Meta:
        model = Dish
        fields = ['profile', 'title', 'receipe', 'dish_ingredients']