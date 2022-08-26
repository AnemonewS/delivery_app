from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('core.auth.urls')),
    path('', include('restaurant.urls')),
    path('', include('customer.urls')),

    path('social-auth/', include('drf_social_oauth2.urls', namespace='drf')),
]
