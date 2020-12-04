from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from bike_auth.forms import SignupForm, LoginForm


def signup(request):
    if request.method == 'GET':
        context = {
            'signup_form': SignupForm(),
        }

        return render(request, 'auth/signup.html', context)
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home page')

        context = {
            'signup_form': form,
        }

        return render(request, 'auth/signup.html', context)


def login_user(request):
    if request.method == 'GET':
        login_form = LoginForm()
        context = {
            'login_form': login_form,
        }

        return render(request, 'auth/login.html', context)
    else:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('home page')

        context = {
            'login_form': login_form,
        }

        return render(request, 'auth/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home page')