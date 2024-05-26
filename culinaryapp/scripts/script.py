import requests

from culinaryapp.models import Dish


def run():
    dishes = Dish.objects.all()
    common_ingredient_list = []

    for dish in dishes:
        for dish_ingredient in dish.dish_ingredients.all():
            print(dish_ingredient.ingredient.title)