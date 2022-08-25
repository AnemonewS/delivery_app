from django.urls import path
from rest_framework.routers import DefaultRouter

from restaurant.views import restaurant_sign_up

router = DefaultRouter()

urlpatterns = [
    path('restaurant/sign_up/', restaurant_sign_up, name='restaurant_sign_up')

]
