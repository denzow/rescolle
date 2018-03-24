from django.urls import path

from .api import views as api_view
from . import views as views
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('index', TemplateView.as_view(template_name='index.html')),
    path('login', TemplateView.as_view(template_name='login.html')),
    path('logout', views.logout_view),

    path('get_coordinate_list', api_view.get_coordinate_list),
    path('get_restaurant/<int:restaurant_id>', api_view.get_restaurant),

    path('request/generate_restaurant/<str:json_serial>', api_view.generate_restaurant_endpoint),
]
