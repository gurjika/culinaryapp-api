from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()

router.register(prefix='dishes', viewset=views.DishViewSet, basename='dish')


ingredients_router = routers.NestedDefaultRouter(parent_router=router, parent_prefix='dishes', lookup='dish')
ingredients_router.register('ingredients', views.IngredientViewSet, basename='ingredient')


urlpatterns = router.urls + ingredients_router.urls