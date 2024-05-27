from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.UserProfile)
admin.site.register(models.Dish)
admin.site.register(models.Ingredient)
admin.site.register(models.Rating)
admin.site.register(models.DishTypeTag)
