# coding: utf-8

from statistics import mean

from .constraints import SourceType
from .models import GnaviRestaurant, CrawlRawData

from .generator import generate_gnavi_restaurant
from .unifier import get_unifier


def get_restaurant_coordinate_list_by_keyword(keyword: str) -> list:
    """
    キーワードを含んだレストランの座標のリストを取得する
    :param keyword:
    :return:
    """
    restaurant_list = GnaviRestaurant.get_list_by_keyword(keyword)
    return [
        {'id': x.id, 'latitude': x.latitude, 'longitude': x.longitude, 'name': x.name}
        for x in restaurant_list
    ]


def get_all_restaurant_coordinate_list() -> list:
    """
    全レストランの座標のリストを戻す
    :return:
    """
    all_restaurant_list = GnaviRestaurant.get_all_valid_list()
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


def get_crawled_data_by_serial(serial: str) -> CrawlRawData:
    return CrawlRawData.get_by_serial(serial)


def generate_restaurant_data(raw_dict_list: list, source_type: SourceType):
    """
    JSONから対応するレストランモデルを構築する
    :param raw_dict_list:
    :param source_type:
    :return:
    """
    restaurant_list = []
    unifier = None
    if source_type.is_gnavi():
        restaurant_list = generate_gnavi_restaurant(raw_dict_list)
        unifier = get_unifier(source_type)

    for restaurant in restaurant_list:
        unified_restaurant = unifier(restaurant)
        print(unified_restaurant.unify())


