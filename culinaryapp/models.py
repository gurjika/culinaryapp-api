from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField('auth.user', on_delete=models.CASCADE, related_name='profile')

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

class Ingredient(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

class Dish(models.Model):
    title = models.CharField(max_length=255)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='dishes')
    receipe = models.TextField()
    ingredient = models.ManyToManyField(Ingredient, through='DishIngredient')


    def __str__(self) -> str:
        return self.title
    

class DishIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='dishes')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish_ingredients')
    quantity = models.FloatField()
    quantity_description = models.CharField(max_length=255)


class DishImage(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()


class ChefProfile(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    bio = models.TextField()
    added_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='chefs')

class Rating(models.Model):
    rating = models.FloatField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='ratings')
    rater = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='rateds')

    def __str__(self) -> str:
        return f'{self.rater} - {self.rating}'


class DishTypeTag(models.Model):
    dish = models.ManyToManyField(Dish, through='DishTag')
    dish_tag = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.dish_tag

class DishTag(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish_tags')
    tag = models.ForeignKey(DishTypeTag, on_delete=models.CASCADE)


class FavouriteDish(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='favourite_dishes')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)