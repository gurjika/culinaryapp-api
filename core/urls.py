from rest_framework.authtoken import views as rest_views
from django.urls import path
from . import views

urlpatterns = [
    path('token/', rest_views.obtain_auth_token, name='obtain-token'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login')
]