from rest_framework.permissions import BasePermission
from rest_framework import permissions
from .models import Dish
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.profile.user == request.user
    
class IsCreatorOfDishOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        dish = Dish.objects.get(id=view.kwargs['dish_pk'])

        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return dish.profile.user == request.user
        