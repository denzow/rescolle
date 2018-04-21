from django.urls import path

from .api import (
    map_related_view,
    collection_related_view,
)
from . import views as views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('index', TemplateView.as_view(template_name='index.html')),
    path('login', TemplateView.as_view(template_name='login.html')),
    path('logout', views.logout_view),

    path('get_coordinate_list', map_related_view.get_coordinate_list),
    path('get_coordinate_list/<int:collection_id>', map_related_view.get_coordinate_list_from_collection_id),
    path('get_restaurant/<int:restaurant_id>', map_related_view.get_restaurant),

    # related collection
    path('get_collection_list/', login_required(collection_related_view.get_collection_list)),
    path('create_collection/', login_required(collection_related_view.create_collection)),
    path('add_restaurant_to_collection/', login_required(collection_related_view.add_restaurant_to_collection)),

    # related crawler
    path('request/generate_restaurant/<str:json_serial>', map_related_view.generate_restaurant_endpoint),
]
