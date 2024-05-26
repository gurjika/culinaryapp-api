from rest_framework import serializers

from culinaryapp.models import Dish, DishIngredient, Ingredient, Rating, UserProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user']


class SimpleDishIngredient(serializers.ModelSerializer):
    class Meta:
        model = DishIngredient
        fields = ['quantity', 'quantity_description']



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
    profile = ProfileSerializer(read_only=True)
    avg_rating = serializers.FloatField(read_only=True)
    
    class Meta:
        model = Dish
        fields = ['id', 'profile', 'title', 'receipe', 'dish_ingredients', 'avg_rating']


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
    

class SimpleDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'title']   

class RatingSerializer(serializers.ModelSerializer):
    dish = SimpleDishSerializer(read_only=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Rating
        fields = ['id','rating', 'dish']

    def create(self, validated_data):
        
        rating, created = Rating.objects.update_or_create(
            id=self.context['user_rating_pk'],
            defaults={
                'rating': validated_data['rating'],
                'dish_id': self.context['dish_pk'],
                'rater': self.context['user'].profile
            }
        )
                

        return rating