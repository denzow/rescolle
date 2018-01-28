# coding: utf-8

from .models import Restaurant


def get_all_restaurant_coordinate_list():
    all_restaurant_list = Restaurant.get_all_list()
    return [
        {'id': x.id, 'latitude': x.latitude, 'longitude': x.longitude, 'name': x.name}
        for x in all_restaurant_list
    ]


