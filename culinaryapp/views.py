from collections import Counter
import random
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from culinaryapp.permissions import IsCreatorOfDishOrReadOnly, IsOwnerOrReadOnly
from culinaryapp.serializers import AddIngredientSerializer, CreateDishSerializer, DishSerializer, ImageSerializer, IngredientSerializer, ProfileSerializer, RatingSerializer, SimpleDishSerializer
from .models import Dish, DishImage, DishIngredient, Ingredient, Rating, UserProfile
from rest_framework.response import Response
from django.db.models import Avg
from rest_framework import generics
# Create your views here.


class DishViewSet(ModelViewSet):
    
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Dish.objects. \
    prefetch_related('dish_ingredients__ingredient', 'dish_ingredients', 'dish_tags__tag'). \
    select_related('profile__user').prefetch_related('images').annotate(avg_rating=Avg('ratings__rating')).all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateDishSerializer
        return DishSerializer

    def get_serializer_context(self):
        return {'user': self.request.user}
    

    @action(detail=True, methods=['GET', 'POST'])
    def rate(self, request, pk):
        if request.method == 'GET':
            current_rating = Rating.objects.filter(
                dish_id=self.kwargs['pk'],
                rater=self.request.user.profile).first()
            if current_rating:
                serializer = RatingSerializer(instance=current_rating)
                return Response(serializer.data)
            else:
                return Response({'detail': 'You have not rated this dish yet.'})
            
        elif request.method == 'POST':
            serializer = RatingSerializer(data=request.data, context={'user': self.request.user, 'dish_pk': self.kwargs['pk']})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)



    

class IngredientViewSet(ModelViewSet):
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

    def get_queryset(self):
        rating = Rating.objects.filter(dish_id=self.kwargs['dish_pk'])

        return rating


    def get_serializer_class(self):
        return RatingSerializer
    

    def get_serializer_context(self):
        user_rating = self.get_queryset().filter(rater=self.request.user.profile).first()

        context = {
            'dish_pk': self.kwargs['dish_pk'], 
            'user': self.request.user,
        }

        if user_rating:
            context['user_rating_pk'] = user_rating.id

        return context

        
class ExploreView(generics.ListAPIView):
    serializer_class = SimpleDishSerializer

    def get_queryset(self):

        
        user_dishes = Dish.objects.filter(profile__user=self.request.user). \
        prefetch_related('dish_ingredients__ingredient', 'dish_ingredients', 'dish_tags__tag') \
        .all()


        try:
            dishes_sample = random.sample(list(user_dishes), 5)
        except ValueError:
            dishes_sample = list(user_dishes)
        
        dish_tags = set()
        dish_ingredients = []

        
        for dish in dishes_sample:
            for ingredient in dish.dish_ingredients.all():
                dish_ingredients.append(ingredient.ingredient)
            for tag in dish.dish_tags.all():
                dish_tags.add(tag.tag)


        ingredient_counts = Counter(dish_ingredients)

        ingredient_sample = [ingredient for ingredient, _ in ingredient_counts.most_common(3)]


        explore_dishes = Dish.objects.filter(dish_tags__tag__in=dish_tags, dish_ingredients__ingredient__in=ingredient_sample).exclude(profile__user=self.request.user).distinct()



        return explore_dishes
        

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        profile = UserProfile.objects.get(user=self.request.user)
        return profile
    
class ImageViewSet(ModelViewSet):
    permission_classes = [IsCreatorOfDishOrReadOnly]

    def get_queryset(self):
        images = DishImage.objects.filter(dish_id=self.kwargs['dish_pk']).all()
        return images
    
    serializer_class = ImageSerializer


    def get_serializer_context(self):
        return {'dish_pk': self.kwargs['dish_pk']}
    

    
