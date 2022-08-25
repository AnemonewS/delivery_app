from django.contrib import admin

from customer.models import DriverProfile, CustomerProfile


@admin.register(DriverProfile)
class DriverProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    pass
