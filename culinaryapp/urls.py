from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()

router.register(prefix='dishes', viewset=views.DishViewSet, basename='dish')


ingredients_router = routers.NestedDefaultRouter(parent_router=router, parent_prefix='dishes', lookup='dish')
ingredients_router.register('ingredients', views.IngredientViewSet, basename='ingredient')


ratings_router = routers.NestedDefaultRouter(parent_router=router, parent_prefix='dishes', lookup='dish')
ratings_router.register('ratings', views.RatingViewSet, basename='rating')


urlpatterns = router.urls + ingredients_router.urls + ratings_router.urls