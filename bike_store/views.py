from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from bike_store.forms import BikeForm, DeleteBikeForm
from bike_store.models import Bike


def home_page(request):
    context = {
        'bikes': Bike.objects.all(),
    }
    return render(request, 'bike_store/bikes.html', context)


def get_new_or_used_bikes(request, is_used):
    bikes = Bike.objects.filter(is_used=is_used)
    context = {
        'bikes': bikes,
    }

    return render(request, 'bike_store/bikes.html', context)


def get_new_bikes(request):
    is_used = False
    return get_new_or_used_bikes(request, is_used)


def get_used_bikes(request):
    is_used = True
    return get_new_or_used_bikes(request, is_used)


@login_required
def sell_a_bike(request):
    user = request.user
    if request.method == 'GET':
        context = {
            'bike_form': BikeForm(),
        }

        return render(request, 'bike_store/sell_a_bike.html', context)
    else:
        bike_form = BikeForm(request.POST,
                             request.FILES)

        if bike_form.is_valid():
            bike = bike_form.save(commit=False)
            bike.user = user
            bike_form.save()
            return redirect('my bikes', user.id)

        context = {
            'bike_form': bike_form,
        }

        return render(request, 'bike_store/sell_a_bike.html', context)


def bike_details(request, pk):
    bike = Bike.objects.get(pk=pk)
    context = {
        'bike': bike,
    }

    return render(request, 'bike_store/bike_details.html', context)


def my_bikes(request, pk):
    user = User.objects.get(pk=pk)
    bikes = Bike.objects.filter(user=user)
    context = {
        'bikes': bikes,
    }

    return render(request, 'bike_store/bikes.html', context)


def edit_bike(request, pk):
    bike = Bike.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'bike_form': BikeForm(instance=bike),
            'bike': bike,
        }

        return render(request, 'bike_store/edit_bike.html', context)
    else:
        bike_form = BikeForm(request.POST,
                             request.FILES,
                             instance=bike)

        if bike_form.is_valid():
            bike_form.save()
            return redirect('my bikes', request.user.id)

        context = {
            'bike_form': bike_form,
            'bike': bike,
        }

        return render(request, 'bike_store/edit_bike.html', context)


def delete_bike(request, pk):
    bike = Bike.objects.get(pk=pk)
    if request.method == 'GET':
        bike_form = DeleteBikeForm(instance=bike)
        context = {
            'bike_form': bike_form,
            'bike': bike,
        }

        return render(request, 'bike_store/delete_bike.html', context)
    else:
        bike.delete()
        return redirect('my bikes', request.user.id)


