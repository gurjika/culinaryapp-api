from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from culinaryapp.serializers import AddIngredientSerializer, CreateDishSerializer, DishSerializer, IngredientSerializer
from .models import Dish, DishIngredient, Ingredient
from rest_framework.response import Response

# Create your views here.


class DishViewSet(ModelViewSet):
    queryset = Dish.objects.prefetch_related('dish_ingredients__ingredient').all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateDishSerializer
        return DishSerializer

    def get_serializer_context(self):
        return {'user': self.request.user}
    



    

class IngredientViewSet(ModelViewSet):
    serializer_class = IngredientSerializer
    http_method_names = ["get", 'post', 'delete', 'head', 'options']

    def get_queryset(self):
        return Ingredient.objects.filter(dishes__dish_id=self.kwargs['dish_pk'])
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddIngredientSerializer
        return IngredientSerializer
    

    def get_serializer_context(self):
        return {'dish_pk': self.kwargs['dish_pk']}
    
    def destroy(self, request, *args, **kwargs):
        dish = Dish.objects.get(id=self.kwargs['dish_pk'])
        ingredient = self.get_object()
        dish.ingredient.remove(ingredient)
        return Response(f'ingredient removed from the list')
    
