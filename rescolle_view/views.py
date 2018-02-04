from django.shortcuts import render
from django.http import JsonResponse

from .components import (
    get_restaurant_coordinate_list_by_keyword,
    get_all_restaurant_coordinate_list,
    get_center_position,
    get_crawled_data_by_serial,
    generate_restaurant_data,
)


def index(request):
    return render(request, 'index.html')


def get_coordinate_list(request):

    keyword = request.GET.get('keyword')
    if keyword:
        restaurant_coordinate_list = get_restaurant_coordinate_list_by_keyword(keyword)
    else:
        restaurant_coordinate_list = get_all_restaurant_coordinate_list()

    return JsonResponse({
        'restaurants': restaurant_coordinate_list,
        'center': get_center_position(restaurant_coordinate_list),
    })


def generate_restaurant_endpoint(request, json_serial):
    crawled_data = get_crawled_data_by_serial(serial=json_serial)
    generate_restaurant_data(crawled_data.json, crawled_data.source_type)
    crawled_data.clear_serial()

    return JsonResponse({
        'status': 'end'
    })
