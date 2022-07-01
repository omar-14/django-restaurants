from django.urls import path
from .views import *

urlpatterns = [
    path('api/restaurant/register', RestaurantsRegister.as_view()),
    path('api/restaurant/delete/<int:id>', RestaurantDelete.as_view()),
    path('api/restaurant/update/<int:id>', RestaurantUpdate.as_view()),
    path('api/restaurant/list', RestaurantList.as_view()),
]