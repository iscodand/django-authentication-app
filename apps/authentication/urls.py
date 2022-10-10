from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('home/', home, name='home'),
]
