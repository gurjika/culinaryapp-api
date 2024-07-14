from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import ChefProfile, Dish, DishImage, FavouriteDish, Ingredient, Rating, UserProfile
from .serializers import CreateDishSerializer, DishSerializer
from django.urls import reverse

User = get_user_model()

class DishViewSetTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.dish = Dish.objects.create(title="Test Dish", profile=self.user.profile)
        self.url = reverse('dish-list')

    def test_list_dishes(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('results' in response.data)

    def test_create_dish(self):
        data = {
            'title': 'New Dish',
            'receipe': 'do'
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dish.objects.count(), 2)

    def test_update_dish(self):
        dish_url = reverse('dish-detail', args=[self.dish.id])
        data = {'title': 'Updated Dish'}
        response = self.client.patch(dish_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.dish.refresh_from_db()
        self.assertEqual(self.dish.title, 'Updated Dish')

    def test_delete_dish(self):
        dish_url = reverse('dish-detail', args=[self.dish.id])
        response = self.client.delete(dish_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Dish.objects.count(), 0)



class RatingViewSetTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.dish = Dish.objects.create(title="Test Dish", profile=self.user.profile)
        self.rating = Rating.objects.create(dish=self.dish, profile=self.user.profile, rating=5)
        self.url = reverse('rating-list', args=[self.dish.id])

    def test_list_ratings(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('results' in response.data)

    def test_add_rating(self):
        data = {'rating': 4}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Rating.objects.count(), 2)

class ExploreViewTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.dish = Dish.objects.create(title="Test Dish", profile=self.user.profile)
        self.url = reverse('explore-list')

    def test_explore_dishes(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('results' in response.data)

class ProfileViewTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.profile = UserProfile.objects.get(user=self.user)
        self.url = reverse('profile')

    def test_retrieve_profile(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user']['id'], self.user.id)




class FavouriteDishViewSetTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.dish = Dish.objects.create(title="Test Dish", profile=self.user.profile, receipe='')
        print(self.dish)
        self.favourite = FavouriteDish.objects.create(profile=self.user.profile, dish=self.dish)
        self.url = reverse('favourite-list')
        token = self.user.auth_token.key
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

    def test_list_favourites(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('results' in response.data)

class ChefViewSetTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.chef = ChefProfile.objects.create(profile=self.user.profile)
        self.url = reverse('chef-list')

    def test_list_chefs(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('results' in response.data)