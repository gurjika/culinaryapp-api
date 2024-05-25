from rest_framework_nested import routers
from . import views


router = routers.NestedDefaultRouter()

router.register('dishes', views.DishViewSet)
