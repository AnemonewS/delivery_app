from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import index

router = DefaultRouter()

urlpatterns = [
    path('', index, name='index')

]
