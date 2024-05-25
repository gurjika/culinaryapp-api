from rest_framework import serializers

from culinaryapp.models import Dish, DishIngredient, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'title']

class DishIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()
    class Meta:
        model = DishIngredient
        fields = ['ingredient', 'quantity', 'quantity_description']

class DishSerializer(serializers.ModelSerializer):
    dish_ingredients = DishIngredientSerializer(many=True)
    class Meta:
        model = Dish
        fields = ['id', 'profile', 'title', 'receipe', 'dish_ingredients']


class CreateDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['title', 'receipe']


    def create(self, validated_data):
        dish = Dish.objects.create(
            profile=self.context['user'].profile,
            title=validated_data['title'], 
            receipe=validated_data['receipe'])
        
        return dish
    


