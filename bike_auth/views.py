from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from django.views.generic.base import View

from bike_auth.forms import SignupForm, LoginForm, ProfileForm
from bike_auth.models import Profile


# @transaction.atomic
# def signup(request):
#     if request.method == 'GET':
#         context = {
#             'signup_form': SignupForm(),
#             'profile_form': ProfileForm(),
#         }
#
#         return render(request, 'auth/register.html', context)
#     else:
#         signup_form = SignupForm(request.POST)
#         profile_form = ProfileForm(request.POST)
#         if signup_form.is_valid() and profile_form.is_valid():
#             user = signup_form.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile_form.save()
#
#             login(request, user)
#             return redirect('home page')
#
#         context = {
#             'signup_form': signup_form,
#             'profile_form': profile_form,
#         }
#
#         return render(request, 'auth/register.html', context)


class Signup(View):
    def get(self, request):
        context = {
                    'signup_form': SignupForm(),
                    'profile_form': ProfileForm(),
                }

        return render(request, 'auth/register.html', context)

    def post(self, request):
        signup_form = SignupForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if signup_form.is_valid() and profile_form.is_valid():
            user = signup_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile_form.save()

            login(request, user)
            return redirect('home page')

        context = {
            'signup_form': signup_form,
            'profile_form': profile_form,
        }

        return render(request, 'auth/register.html', context)


def get_next_url(params):
    next_url = params.get('next')
    return next_url if next_url != '' else 'home page'


# def login_user(request):
#     if request.method == 'GET':
#         login_form = LoginForm()
#         context = {
#             'login_form': login_form,
#         }
#
#         return render(request, 'auth/login.html', context)
#     else:
#         login_form = LoginForm(request.POST)
#         next_url = get_next_url(request.POST)
#
#         if login_form.is_valid():
#             username = login_form.cleaned_data['username']
#             password = login_form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#
#             if user:
#                 login(request, user)
#                 return redirect(next_url)
#
#         context = {
#             'login_form': login_form,
#         }
#
#         return render(request, 'auth/login.html', context)


class Login(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form,
        }

        return render(request, 'auth/login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        next_url = get_next_url(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect(next_url)

        context = {
            'login_form': login_form,
        }

        return render(request, 'auth/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home page')


def get_my_profile(request, pk):
    user = User.objects.get(pk=pk)
    profile = Profile.objects.get(user_id=user.id)
    context = {
        'profile': profile,
        'user': user,
    }

    return render(request, 'auth/profile.html', context)


def update_my_profile(request, pk):
    user = User.objects.get(pk=pk)
    profile = Profile.objects.get(user=user)
    if request.method == 'GET':
        profile_form = ProfileForm(instance=profile)

        context = {
            'profile_form': profile_form,
            'user': user,
        }

        return render(request, 'auth/profile_update.html', context)
    else:
        profile_form = ProfileForm(request.POST,
                                   request.FILES,
                                   instance=profile)

        if profile_form.is_valid():
            profile_form.save()

            return redirect('my profile', pk)

        context = {
            'profile_form': profile_form,
            'profile': profile,
        }

        return render(request, 'auth/profile_update.html', context)


def get_profile_of_bike_owner(request, pk):
    owner = User.objects.get(pk=pk)
    owner_profile = Profile.objects.get(user_id=owner.id)
    context = {
        'owner': owner,
        'owner_profile': owner_profile,
    }

    return render(request,'auth/profile.html', context)









