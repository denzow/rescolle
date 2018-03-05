# coding: utf-8
from statistics import mean
from .models import UnifiedRestaurant


def get_restaurant_coordinate_list_by_keyword(keyword: str) -> list:
    """
    キーワードを含んだレストランの座標のリストを取得する
    :param keyword:
    :return:
    """
    restaurant_list = UnifiedRestaurant.get_list_by_keyword(keyword)
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
    avg_latitude = mean([x['latitude'] for x in position_list])
    avg_longitude = mean([x['longitude'] for x in position_list])
    return {'latitude': avg_latitude, 'longitude': avg_longitude}