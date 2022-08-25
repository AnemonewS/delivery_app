from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import index, sign_up
from django.contrib.auth import views as auth_views

router = DefaultRouter()

urlpatterns = [
    path('', index, name='index'),

    path('auth/sign_in/', auth_views.LoginView.as_view(template_name='account/sign_in.html'), name='sign_in'),
    path('auth/sign_out/', auth_views.LogoutView.as_view(next_page='/'), name='sign_out'),
    path('auth/sign_up/', sign_up, name='sign_up'),
]
