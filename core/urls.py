from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import index, user_account, meal, order, report

router = DefaultRouter()

urlpatterns = [
    path('', index, name='index'),
    path('restaurant/account/', user_account, name='user_account'),
    path('restaurant/meal/', meal, name='meal'),
    path('restaurant/order/', order, name='order'),
    path('restaurant/report/', report, name='report'),
]
