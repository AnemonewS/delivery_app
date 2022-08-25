from django.shortcuts import render, redirect

from core.forms import RestaurantForm


def restaurant_sign_up(request):
    rest_form = RestaurantForm()

    if request.method == 'POST':
        rest_form = RestaurantForm(request.POST, request.FILES)

        if rest_form.is_valid():
            new_restaurant = rest_form.save(commit=False)
            new_restaurant.save()

            return redirect('/')

    return render(request, 'restaurant/sign_up.html', {'rest_form': rest_form})
