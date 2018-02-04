from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('index', index),
    path('get_coordinate_list', get_coordinate_list),

    path('request/generate_restaurant/<str:json_serial>', generate_restaurant_endpoint),
]
