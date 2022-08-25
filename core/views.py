from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from core.forms import UserForm, RestaurantForm
from core.models import User


@login_required(login_url='/auth/sign_in/')
def index(request):
    return render(request, 'index.html')


def sign_up(request):
    user_form = UserForm()
    rest_form = RestaurantForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        rest_form = RestaurantForm(request.POST, request.FILES)

        if user_form.is_valid() and rest_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_restaurant = rest_form.save(commit=False)
            new_restaurant.user = new_user
            new_restaurant.save()

            login(request, authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password']
            ))

            return redirect('/')

    return render(request, 'account/sign_up.html',
                  {'user_form': user_form,
                   'rest_form': rest_form})
