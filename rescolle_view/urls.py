from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('index', index),
    path('get_coordinate_list', get_coordinate_list),

]
