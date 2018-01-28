from django.shortcuts import render
from django.http import JsonResponse

from .components import get_all_restaurant_coordinate_list


def index(request):
    return render(request, 'index.html')


def get_coordinate_list(request):
    return JsonResponse({'result': get_all_restaurant_coordinate_list()})

