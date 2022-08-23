from django.contrib import admin

from core.models import User


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'role']
    list_display_links = ['first_name', 'last_name', 'email', 'role']
