from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField('auth.user', on_delete=models.CASCADE, related_name='profile')

class Ingredient(models.Model):
    
    title = models.CharField(max_length=255)

class Dish(models.Model):
    title = models.CharField(max_length=255)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='dishes')
    receipe = models.TextField()
    ingredient = models.ManyToManyField(Ingredient, through='DishIngredient')
    

class DishIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='dishes')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish_ingredients')
    quantity = models.FloatField()
    quantity_description = models.CharField(max_length=255)


class DishImage(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    image = models.ImageField()


class ChefProfile(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    bio = models.TextField()


class Rating(models.Model):
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)