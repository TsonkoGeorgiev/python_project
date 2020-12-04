from django.urls import path

from bike_auth.views import signup, login_user, logout_user

urlpatterns = [
    path('signup/', signup, name='sign up'),
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
]
