from django.urls import path
from .views import *

urlpatterns = [
    path('user/', Users.as_view()),
    path('user/get', GetUser.as_view()),
]