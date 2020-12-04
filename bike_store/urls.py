from django.urls import path

from bike_store.views import home_page, get_new_bikes, get_used_bikes, sell_a_bike

urlpatterns = [
    path('', home_page, name='home page'),
    path('new-bikes/', get_new_bikes, name='new bikes'),
    path('used-bikes/', get_used_bikes, name='used bikes'),
    path('sell-a-bike/', sell_a_bike, name='sell a bike'),
]
