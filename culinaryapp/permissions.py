from rest_framework.permissions import BasePermission
from rest_framework import permissions
from .models import ChefProfile, Dish


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.profile.user == request.user

    
class IsCreatorOfDishOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        dish = Dish.objects.get(id=view.kwargs['dish_pk'])

        if request.method in permissions.SAFE_METHODS:
            return True

        return dish.profile.user == request.user
        

class IsCreatorOfChefOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
 

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.added_by.user == request.user