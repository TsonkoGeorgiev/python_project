from django.urls import path

from bike_auth.views import signup, login_user, logout_user, get_my_profile, update_my_profile

urlpatterns = [
    path('signup/', signup, name='sign up'),
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('my-profile/<int:pk>/', get_my_profile, name='my profile'),
    path('update-my-profile/<int:pk>/', update_my_profile, name='profile update'),
]
