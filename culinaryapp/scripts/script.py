import random
import requests
from collections import Counter

from culinaryapp.models import Dish, DishIngredient, DishTag, DishTypeTag, Ingredient


def run():
    # dishes = Dish.objects.all()
    # common_ingredient_list = []

    # headers = {
    #     'x-api-key': 'e6d15d67219f4bad987638b89e5967bc',
    # }

    # params = {
    #     'number': 25,
    # }
    
    # receipes = requests.get(url='https://api.spoonacular.com/recipes/complexSearch', headers=headers, params=params)
    # receipes = receipes.json()

    # for recipe in receipes['results']:
        
    #     dish = Dish.objects.create(title=recipe['title'], profile_id=1, receipe='Cook The Thing')
    #     id = recipe['id']
    #     ingredients = requests.get(url=f'https://api.spoonacular.com/recipes/{id}/ingredientWidget.json', headers=headers)
    #     for ingredient in ingredients.json()['ingredients']:
    #         ingredient_created, created = Ingredient.objects.get_or_create(title=ingredient['name'])
    #         DishIngredient.objects.create(
    #             dish=dish, 
    #             ingredient=ingredient_created, 
    #             quantity=ingredient['amount']['metric']['value'], 
    #             quantity_description=ingredient['amount']['metric']['unit'])


    # Dish names
    # dish_names = [
    #     "Red Lentil Soup with Chicken and Turnips",
    #     "Asparagus and Pea Soup: Real Convenience Food",
    #     "Garlicky Kale",
    #     "Slow Cooker Beef Stew",
    #     "Red Kidney Bean Jambalaya",
    #     "Cauliflower, Brown Rice, and Vegetable Fried Rice",
    #     "Quinoa and Chickpea Salad with Sun-Dried Tomatoes and Dried Cherries",
    #     "Easy Homemade Rice and Beans",
    #     "Tuscan White Bean Soup with Olive Oil and Rosemary",
    #     "Crunchy Brussels Sprouts Side Dish",
    #     "Turkey Tomato Cheese Pizza",
    #     "Nigerian Snail Stew",
    #     "Slow Cooker: Pork and Garbanzo Beans",
    #     "Powerhouse Almond Matcha Superfood Smoothie",
    #     "Broccolini Quinoa Pilaf",
    #     "Easy To Make Spring Rolls",
    #     "Farro With Mushrooms and Asparagus",
    #     "Butternut Squash Frittata",
    #     "Herbivoracious' White Bean and Kale Soup",
    #     "Tomato and lentil soup",
    #     "Swiss Chard Wraps",
    #     "Corn Avocado Salsa",
    #     "Cheesy Chicken Enchilada Quinoa Casserole",
    #     "Zesty Green Pea and Jalapeño Pesto Pasta",
    #     "Jade Buddha Salmon Tartare"
    # ]

    # # Dictionary to map keywords to tags
    # tag_map = {
    #     "soup": ["soup"],
    #     "asparagus": ["vegetable", "green"],
    #     "kale": ["vegetable", "leafy green"],
    #     "stew": ["stew"],
    #     "jambalaya": ["spicy"],
    #     "fried rice": ["rice", "stir-fry"],
    #     "salad": ["salad"],
    #     "rice and beans": ["rice", "beans"],
    #     "white bean soup": ["soup", "bean"],
    #     "brussels sprouts": ["vegetable", "side dish"],
    #     "pizza": ["italian"],
    #     "snail stew": ["exotic"],
    #     "pork and garbanzo beans": ["pork", "bean"],
    #     "smoothie": ["beverage"],
    #     "quinoa pilaf": ["quinoa", "side dish"],
    #     "spring rolls": ["appetizer"],
    #     "farro with mushrooms and asparagus": ["grain", "vegetable"],
    #     "butternut squash frittata": ["vegetable", "egg"],
    #     "white bean and kale soup": ["soup", "bean"],
    #     "tomato and lentil soup": ["soup", "lentil"],
    #     "swiss chard wraps": ["vegetable", "wrap"],
    #     "corn avocado salsa": ["salsa", "avocado"],
    #     "cheesy chicken enchilada quinoa casserole": ["casserole", "cheese", "chicken"],
    #     "zesty green pea and jalapeño pesto pasta": ["pasta", "pea", "pesto"],
    #     "jade buddha salmon tartare": ["salmon", "appetizer"]
    # }


    # for key, value in tag_map.items():
    #     for tag in tag_map[key]:
    #         tag, created = DishTypeTag.objects.get_or_create(dish_tag=tag)


    
    # dishes = Dish.objects.all()
    # # Function to generate tags based on dish names
    
    # tags = []
    # for dish in dishes:
    #     dish_tags = set()
    #     for keyword, tag_list in tag_map.items():
    #         if keyword.lower() in dish.title.lower():
    #             for tag in tag_list:
    #                 tag = DishTypeTag.objects.get(dish_tag=tag)
    #                 DishTag.objects.create(dish=dish, tag=tag)
    #     tags.append((dish.title, list(dish_tags)))  
    


    # for dish_name, dish_tags in tags:
    #     print(f"Dish: {dish_name} -> Tags: {', '.join(dish_tags)}")



    pass




        