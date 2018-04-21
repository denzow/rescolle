import json
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rescolle_view.collection import service as collection_sv


def create_collection(request):
    user_id = request.user.id
    data = json.loads(request.body)
    collection = collection_sv.create_collection(
        name=data['name'],
        description=data['description'],
        owner_id=user_id
    )
    return JsonResponse({'collection_id': collection.id})


def add_restaurant_to_collection(request):
    user_id = request.user.id
    data = json.loads(request.body)

    collection = collection_sv.get_collection(data['collection_id'])
    if collection.owner_id != user_id:
        return HttpResponse({'error': True}, status=500)

    added_restaurant = collection_sv.add_restaurant_to_collection(
        collection_id=data['collection_id'],
        restaurant_id=data['restaurant_id'],
        memo=data['memo'],
    )
    return JsonResponse({'restaurant_id': added_restaurant.id})


def get_collection_list(request):
    user_id = request.user.id
    collection_list = collection_sv.get_collection_data_by_owner_id(user_id)

    return JsonResponse({'collection_list': collection_list})
