from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from culinaryapp.serializers import CreateDishSerializer, DishSerializer, IngredientSerializer
from .models import Dish, Ingredient
# Create your views here.


class DishViewSet(ModelViewSet):
    queryset = Dish.objects.prefetch_related('dish_ingredients__ingredient').all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DishSerializer
        elif self.request.method == 'POST':
            return CreateDishSerializer

    def get_serializer_context(self):
        return {'user': self.request.user}
    

class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer