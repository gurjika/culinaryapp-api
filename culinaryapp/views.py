from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Dish
# Create your views here.


class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = 