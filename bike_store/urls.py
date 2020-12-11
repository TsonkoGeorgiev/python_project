from django.urls import path

from bike_store.views import home_page, sell_a_bike, bike_details, edit_bike, \
    delete_bike, MyBikes

urlpatterns = [
    path('', home_page, name='home page'),
    path('sell-a-bike/', sell_a_bike, name='sell a bike'),
    path('bike-details/<int:pk>/', bike_details, name='bike details'),
    # path('my-bikes/<int:pk>/', my_bikes, name='my bikes'),
    path('my-bikes/<int:pk>/', MyBikes.as_view(), name='my bikes'),
    path('edit-bike/<int:pk>/', edit_bike, name='edit bike'),
    path('delete-bike/<int:pk>/', delete_bike, name='delete bike'),
]
