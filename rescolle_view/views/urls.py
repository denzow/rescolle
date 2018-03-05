from django.urls import path

from rescolle_view.views.views import *

urlpatterns = [
    path('', index),
    path('index', index),

    path('request/generate_restaurant/<str:json_serial>', generate_restaurant_endpoint),
]
