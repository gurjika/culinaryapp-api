from rest_framework import serializers

from culinaryapp.models import Dish, DishIngredient, Ingredient

class SimpleDishIngredient(serializers.ModelSerializer):
    class Meta:
        model = DishIngredient
        fields = [ 'quantity', 'quantity_description']


class IngredientSerializer(serializers.ModelSerializer):
    dishes = SimpleDishIngredient(read_only=True, many=True)
    class Meta:
        model = Ingredient
        fields = ['id', 'title', 'dishes']

class DishIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()
    class Meta:
        model = DishIngredient
        fields = ['ingredient', 'quantity', 'quantity_description']

class DishSerializer(serializers.ModelSerializer):
    dish_ingredients = DishIngredientSerializer(many=True, read_only=True)
    profile = serializers.PrimaryKeyRelatedField(read_only=True)

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
    

class AddIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishIngredient
        fields = ['ingredient', 'quantity', 'quantity_description']



    def create(self, validated_data):
        
        dish_ingredient = DishIngredient.objects.create(
            dish_id=self.context['dish_pk'],
            ingredient=validated_data['ingredient'],
            quantity=validated_data['quantity'],
            quantity_description=validated_data['quantity_description'])
        
        return dish_ingredient
    
    
