from django.urls import path
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()

router.register(prefix='dishes', viewset=views.DishViewSet, basename='dish')
router.register(prefix='favourites', viewset=views.FavouriteDishViewSet, basename='favourite')

ingredients_router = routers.NestedDefaultRouter(parent_router=router, parent_prefix='dishes', lookup='dish')
ingredients_router.register('ingredients', views.IngredientViewSet, basename='ingredient')


ratings_router = routers.NestedDefaultRouter(parent_router=router, parent_prefix='dishes', lookup='dish')
ratings_router.register('ratings', views.RatingViewSet, basename='rating')


images_router = routers.NestedDefaultRouter(parent_router=router, parent_prefix='dishes', lookup='dish')
images_router.register('images', views.ImageViewSet, basename='image')

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('explore/', views.ExploreView.as_view(), name='explore')
]

urlpatterns += router.urls + ingredients_router.urls + ratings_router.urls + images_router.urls