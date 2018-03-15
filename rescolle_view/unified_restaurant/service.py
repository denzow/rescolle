# coding: utf-8
from statistics import mean
from .models import UnifiedRestaurant
from rescolle_view.tag import service as tag_sv


def get_restaurant_coordinate_list_by_keyword(keyword: str) -> list:
    """
    キーワードを含んだレストランの座標のリストを取得する
    :param keyword:
    :return:
    """
    restaurant_id_list = tag_sv.get_restaurant_by_tag_keyword(keyword)
    print(restaurant_id_list)
    restaurant_list = UnifiedRestaurant.get_list_by_id_list(restaurant_id_list)
    print(restaurant_list)
    return [
        {'id': x.id, 'latitude': x.latitude, 'longitude': x.longitude, 'name': x.name}
        for x in restaurant_list
    ]


def get_all_restaurant_coordinate_list() -> list:
    """
    全レストランの座標のリストを戻す
    :return:
    """
    all_restaurant_list = UnifiedRestaurant.get_all_valid_list()
    return [
        {'id': x.id, 'latitude': x.latitude, 'longitude': x.longitude, 'name': x.name}
        for x in all_restaurant_list
    ]


def get_center_position(position_list) -> dict:
    """
    座標の中心点を求める
    :param position_list:
    :return:
    """
    from pprint import pprint
    pprint(position_list)
    if not position_list:
        return  {'latitude': None, 'longitude': None}
    avg_latitude = mean([x['latitude'] for x in position_list])
    avg_longitude = mean([x['longitude'] for x in position_list])
    return {'latitude': avg_latitude, 'longitude': avg_longitude}
