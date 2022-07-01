from django.urls import path
from .views import *

urlpatterns = [
    path('api/user/register', Users.as_view()),
    path('api/user/login', LoginUser.as_view()),
    path('user/get', GetUser.as_view()),
]