from django.urls import path

from bike_auth.views import logout_user, get_my_profile, update_my_profile, \
    get_profile_of_bike_owner, Signup, Login

urlpatterns = [
    # path('signup/', signup, name='sign up'),
    path('signup/', Signup.as_view(), name='sign up'),
    # path('login/', login_user, name='login user'),
    path('login/', Login.as_view(), name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('my-profile/<int:pk>/', get_my_profile, name='my profile'),
    path('update-my-profile/<int:pk>/', update_my_profile, name='profile update'),
    path('profile/<int:pk>/', get_profile_of_bike_owner, name='profile of bike owner'),
]
