from collections import Counter
import random
from django_filters.rest_framework import DjangoFilterBackend

import traceback
from django.db import connection
from django.shortcuts import get_object_or_404, render
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action
from culinaryapp.permissions import IsCreatorOfDishOrReadOnly, IsOwnerOrReadOnly
from culinaryapp.serializers import AddIngredientSerializer, ChefSerializer, CreateDishSerializer, DishSerializer, ExploreSerializer, FavouriteDishCreateSerializer, FavouriteDishSerializer, ImageSerializer, IngredientSerializer, ProfileSerializer, RatingSerializer, SimpleDishSerializer
from .models import ChefProfile, Dish, DishImage, DishIngredient, FavouriteDish, Ingredient, Rating, UserProfile
from rest_framework.response import Response
from django.db.models import Avg
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework import generics
# Create your views here.


class DishViewSet(ModelViewSet):

    """
    ViewSet for managing dishes.

    This view provides CRUD operations for dishes. It allows creating, retrieving, updating, and deleting dishes.
    The queryset is optimized by prefetching related ingredients, tags, and images, and annotating the average rating.
    
    - `permission_classes`: Ensures that only the owner can modify a dish.
    - `queryset`: Prefetches related ingredients, tags, and images, and annotates the average rating.
    - `get_serializer_class`: Returns `CreateDishSerializer` for POST requests and `DishSerializer` for others.
    - `get_serializer_context`: Adds the current user to the serializer context.
    - `filter_backends`: Allows filtering dishes by title and tags.
    """
    
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    queryset = Dish.objects. \
    prefetch_related('dish_ingredients__ingredient', 'dish_ingredients', 'dish_tags__tag'). \
    select_related('profile__user').prefetch_related('images').annotate(avg_rating=Avg('ratings__rating')).all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateDishSerializer
        return DishSerializer

    def get_serializer_context(self):
        return {'user': self.request.user}
    

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'dish_tags']


    # @action(detail=True, methods=['GET', 'POST'])
    # def rate(self, request, pk):
    #     if request.method == 'GET':
    #         current_rating = Rating.objects.filter(
    #             dish_id=self.kwargs['pk'],
    #             rater=self.request.user.profile).first()
    #         if current_rating:
    #             serializer = RatingSerializer(instance=current_rating)
    #             return Response(serializer.data)
    #         else:
    #             return Response({'detail': 'You have not rated this dish yet.'})
            
    #     elif request.method == 'POST':
    #         serializer = RatingSerializer(data=request.data, context={'user': self.request.user, 'dish_pk': self.kwargs['pk']})
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)



    

class IngredientViewSet(ModelViewSet):
    """
    ViewSet for managing ingredients of a dish.

    This view provides operations to list, add, and delete ingredients for a specific dish.
    
    - `permission_classes`: Ensures that only the creator of the dish can modify its ingredients.
    - `serializer_class`: Uses `IngredientSerializer` for GET requests and `AddIngredientSerializer` for POST requests.
    - `get_queryset`: Returns ingredients related to a specific dish.
    - `get_serializer_context`: Adds the dish ID to the serializer context.
    - `destroy`: Removes an ingredient from a dish.
    """
    permission_classes = [IsCreatorOfDishOrReadOnly]
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
    


class RatingViewSet(ModelViewSet):
    """
    ViewSet for managing ratings of a dish.

    This view provides operations to list and add ratings for a specific dish.
    
    - `permission_classes`: Ensures that only authenticated users can rate and only the owner can modify their ratings.
    - `get_queryset`: Returns ratings related to a specific dish.
    - `get_serializer_class`: Returns `RatingSerializer`.
    - `get_serializer_context`: Adds the dish ID and current user to the serializer context.
    """

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def get_queryset(self):
        dish = get_object_or_404(Dish, id=self.kwargs['dish_pk'])
        ratings = Rating.objects.select_related('profile__user').select_related('dish').filter(dish=dish).all()
        return ratings


    def get_serializer_class(self):
        return RatingSerializer
    


    def get_serializer_context(self):
        
        context = {
            'dish_pk': self.kwargs['dish_pk'], 
            'user': self.request.user,
        }


        return context

        
class ExploreView(ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    """
    View for exploring dishes based on user preferences.

    This view provides a list of dishes similar to those liked by the user.
    
    - `serializer_class`: Uses `ExploreSerializer` for the response.
    - `get_queryset`: Returns a sample of dishes based on the user's preferred ingredients and tags.
    """
    serializer_class = ExploreSerializer

    def get_queryset(self):
        user_dishes = Dish.objects.filter(profile__user=self.request.user). \
        prefetch_related('dish_ingredients__ingredient', 'dish_ingredients', 'dish_tags__tag')
        
        user_dishes_list = list(user_dishes)

        try:
            dishes_sample = random.sample(user_dishes_list, 5)
        except ValueError:
            dishes_sample = user_dishes_list

        
        dish_tags = set()
        dish_ingredients = []

        
        for dish in dishes_sample:
            for ingredient in dish.dish_ingredients.all():
                dish_ingredients.append(ingredient.ingredient)
            for tag in dish.dish_tags.all():
                dish_tags.add(tag.tag)


        ingredient_counts = Counter(dish_ingredients)

        ingredient_sample = [ingredient for ingredient, _ in ingredient_counts.most_common(3)]


        explore_dishes = Dish.objects.filter(dish_tags__tag__in=dish_tags, dish_ingredients__ingredient__in=ingredient_sample).select_related('profile__user').exclude(profile__user=self.request.user).distinct().all()


        return explore_dishes
        

class ProfileView(generics.RetrieveUpdateAPIView):
    """
    View for retrieving and updating user profiles.

    This view provides operations to retrieve and update the profile of the authenticated user.
    
    - `permission_classes`: Ensures that only authenticated users can access this view.
    - `serializer_class`: Uses `ProfileSerializer`.
    - `get_object`: Returns the profile of the authenticated user.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        profile = UserProfile.objects.get(user=self.request.user)
        return profile
    
class ImageViewSet(ModelViewSet):
    """
    ViewSet for managing images of a dish.

    This view provides operations to list and add images for a specific dish.
    
    - `permission_classes`: Ensures that only the creator of the dish can modify its images.
    - `get_queryset`: Returns images related to a specific dish.
    - `serializer_class`: Uses `ImageSerializer`.
    - `get_serializer_context`: Adds the dish ID to the serializer context.
    """
    permission_classes = [IsCreatorOfDishOrReadOnly]

    def get_queryset(self):
        dish = get_object_or_404(Dish, id=self.kwargs['dish_pk'])
        images = DishImage.objects.select_related('dish').filter(dish=dish).all()
        return images
    
    serializer_class = ImageSerializer


    def get_serializer_context(self):
        return {'dish_pk': self.kwargs['dish_pk']}
    

    
class FavouriteDishViewSet(ModelViewSet):
    """
    ViewSet for managing favourite dishes of a user.

    This view provides operations to list and add favourite dishes for the authenticated user.
    
    - `permission_classes`: Ensures that only authenticated users can access this view.
    - `get_queryset`: Returns favourite dishes of the authenticated user.
    - `get_serializer_context`: Adds the current user to the serializer context.
    - `get_serializer_class`: Uses `FavouriteDishCreateSerializer` for POST requests and `FavouriteDishSerializer` for others.
    """
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FavouriteDish.objects.filter(profile__user=self.request.user).all()

    def get_serializer_context(self):
        return {'user': self.request.user}

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FavouriteDishCreateSerializer
        return FavouriteDishSerializer
    


class ChefViewSet(ModelViewSet):
    """
    ViewSet for managing chef profiles.

    This view provides operations to list and retrieve chef profiles.
    
    - `permission_classes`: Ensures that only authenticated users can access this view, and only the owner can modify it.
    - `serializer_class`: Uses `ChefSerializer`.
    - `get_queryset`: Returns all chef profiles.
    - `get_serializer_context`: Adds the current user to the serializer context.
    """
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = ChefSerializer

    def get_queryset(self):
        
        return ChefProfile.objects.select_related('profile__user').all()

    def get_serializer_context(self):
        return {'user': self.request.user}