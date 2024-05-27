from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from culinaryapp.permissions import IsCreatorOfDishOrReadOnly, IsOwnerOrReadOnly
from culinaryapp.serializers import AddIngredientSerializer, CreateDishSerializer, DishSerializer, ImageSerializer, IngredientSerializer, ProfileSerializer, RatingSerializer
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
        return {'dish_pk': self.kwargs['dish_pk'], 'user': self.request.user, 'user_rating_pk': user_rating.id}

        
class ExploreView(generics.ListAPIView):

    def get_queryset(self):

        dishes = Dish.objects.all()

        common_ingredient_list = []

        for dish in dishes:
            for dish_ingredient in dish.dish_ingredients:
                print(dish_ingredient)

        return super().get_queryset()
    

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