from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/auth/sign_in/')
def index(request):
    return render(request, 'index.html')


@login_required(login_url='/auth/sign_in/')
def user_account(request):
    return render(request, 'restaurant/user_account.html', {})


@login_required(login_url='/auth/sign_in/')
def meal(request):
    return render(request, 'restaurant/meal.html', {})


@login_required(login_url='/auth/sign_in/')
def order(request):
    return render(request, 'restaurant/order.html', {})


@login_required(login_url='/auth/sign_in/')
def report(request):
    return render(request, 'restaurant/report.html', {})
