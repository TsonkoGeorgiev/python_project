from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from bike_store.forms import BikeForm, DeleteBikeForm, FilterForm
from bike_store.models import Bike


def get_initial_filters(params):
    make = params['make'] if 'make' in params else ''
    reg_year = params['reg_year'] if 'reg_year' in params else ''
    mileage = params['mileage'] if 'mileage' in params else ''
    engine_size = params['engine_size'] if 'engine_size' in params else ''
    body_type = params['body_type'] if 'body_type' in params else ''
    price = params['price'] if 'price' in params else ''
    is_used = params['is_used'] if 'is_used' in params else ''

    return {
        'make': make,
        'reg_year': reg_year,
        'mileage': mileage,
        'engine_size': engine_size,
        'body_type': body_type,
        'price': price,
        'is_used': is_used
    }


def get_modified_filters(params):
    make = params['make'] if 'make' in params else ''
    reg_year = int(params['reg_year']) if 'reg_year' in params and params['reg_year'] != '' else ''

    mileage = params['mileage'] if 'mileage' in params else ''
    if mileage != '' and mileage != 'any':
        mileage_le = int(mileage[:mileage.find('-')])
        mileage_ue = int(mileage[mileage.find('-') + 1:])
        mileage__range = [mileage_le, mileage_ue]
    else:
        mileage__range = ''

    engine_size = params['engine_size'] if 'engine_size' in params else ''
    if engine_size != '' and engine_size != 'any':
        engine_size_le = int(engine_size[:engine_size.find('-')])
        engine_size_ue = int(engine_size[engine_size.find('-') + 1:])
        engine_size__range = [engine_size_le, engine_size_ue]
    else:
        engine_size__range = ''

    body_type = params['body_type'] if 'body_type' in params else ''

    price = params['price'] if 'price' in params else ''
    if price != '' and price != 'any':
        price_le = int(price[:price.find('-')])
        price_ue = int(price[price.find('-') + 1:])
        price__range = [price_le, price_ue]
    else:
        price__range = ''

    if 'is_used' in params and params['is_used'] == 'used':
        is_used = True
    elif 'is_used' in params and params['is_used'] == 'new':
        is_used = False
    else:
        is_used = ''

    return {
        'make': make,
        'reg_year': reg_year,
        'mileage__range': mileage__range,
        'engine_size__range': engine_size__range,
        'body_type': body_type,
        'price__range': price__range,
        'is_used': is_used
    }


def home_page(request):
    filter_form = FilterForm(request.GET)
    if filter_form.is_valid():
        params_initial = get_initial_filters(request.GET)
        filter_form = FilterForm(initial=params_initial)
        params_modified = get_modified_filters(request.GET)
        params_modified = {k: v for (k, v) in params_modified.items() if v != '' and v != 'any'}
        context = {
            'bikes': Bike.objects.filter(**params_modified),
            'filter_form': filter_form,
            'view': 'home_page',
        }
        return render(request, 'bike_store/bikes.html', context)

    context = {
        'bikes': Bike.objects.all(),
        'filter_form': filter_form,
        'view': 'home_page',
    }
    return render(request, 'bike_store/bikes.html', context)


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
        'is_owner': bike.user_id == request.user.id,
        'owner': User.objects.get(pk=bike.user_id),
    }

    return render(request, 'bike_store/bike_details.html', context)


# def my_bikes(request, pk):
#     filter_form = FilterForm()
#     user = User.objects.get(pk=pk)
#     bikes = Bike.objects.filter(user=user)
#     context = {
#         'bikes': bikes,
#         'filter_form': filter_form,
#     }
#
#     return render(request, 'bike_store/bikes.html', context)


class MyBikes(DetailView):
    model = User
    template_name = 'bike_store/bikes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = context['user']
        context['bikes'] = Bike.objects.filter(user=user)
        return context


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
