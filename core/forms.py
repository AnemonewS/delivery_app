from django import forms
from .models import User
from restaurant.models import Restaurant


class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=200, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'email')


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('title', 'phone', 'address', 'logo')
