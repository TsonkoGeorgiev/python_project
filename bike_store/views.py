from django.shortcuts import render, redirect

from bike_store.forms import BikeForm
from bike_store.models import Bike


def home_page(request):
    context = {
        'bikes': Bike.objects.all(),
    }
    return render(request, 'bike_store/home_page.html', context)


def get_new_or_used_bikes(request, is_used):
    bikes = Bike.objects.filter(is_used=is_used)
    context = {
        'bikes': bikes,
    }

    return render(request, 'bike_store/home_page.html', context)


def get_new_bikes(request):
    is_used = False
    return get_new_or_used_bikes(request, is_used)


def get_used_bikes(request):
    is_used = True
    return get_new_or_used_bikes(request, is_used)


def sell_a_bike(request):
    if request.method == 'GET':
        context = {
            'bike_form': BikeForm(),
        }

        return render(request, 'bike_store/sell_a_bike.html', context)
    else:
        bike_form = BikeForm(request.POST,
                             request.FILES)

        if bike_form.is_valid():
            bike_form.save()
            return redirect('home page')

        context = {
            'bike_form': bike_form,
        }

        return render(request, 'bike_store/sell_a_bike.html', context)








