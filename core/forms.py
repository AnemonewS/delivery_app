from django import forms
from .models import User
from restaurant.models import Restaurant


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=200, required=True,
                               widget=forms.TextInput(attrs={'required': 'True'}), label="Логин")
    email = forms.CharField(max_length=200, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'email')


class RestaurantForm(forms.ModelForm):
    phone = forms.CharField(max_length=200, label='Номер телефона', widget=forms.TextInput())
    title = forms.CharField(max_length=150, label='Название ресторана', widget=forms.TextInput())

    class Meta:
        model = Restaurant
        fields = ('title', 'phone', 'address', 'logo')
