# coding: utf-8
from statistics import mean
from .models import UnifiedRestaurant
from rescolle_view.tag import service as tag_sv


def get_restaurant_coordinate_list_by_keyword(keyword: str, north_east_lat=None, north_east_lng=None, south_west_lat=None, south_west_lng=None) -> list:
    """
    指定座標内のキーワードを含んだレストランの座標のリストを取得する
    :param keyword:
    :return:
    """
    restaurant_id_list = tag_sv.get_restaurant_by_tag_keyword(keyword)
    if all([north_east_lat, north_east_lng, south_west_lat, south_west_lng]):
        # 表示範囲より少し広めに取る
        restaurant_list = UnifiedRestaurant.get_list_by_id_list_with_coordinate(
            id_list=restaurant_id_list,
            north_east_lat=north_east_lat + 0.005,
            north_east_lng=north_east_lng + 0.005,
            south_west_lat=south_west_lat - 0.005,
            south_west_lng=south_west_lng - 0.005,
        )
    else:
        restaurant_list = UnifiedRestaurant.get_list_by_id_list(restaurant_id_list)
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
    if not position_list:
        return {'latitude': None, 'longitude': None}
    avg_latitude = mean([x['latitude'] for x in position_list])
    avg_longitude = mean([x['longitude'] for x in position_list])
    return {'latitude': avg_latitude, 'longitude': avg_longitude}


def get_restaurant_info(restaurant_id: int):
    restaurant = UnifiedRestaurant.get_by_id(restaurant_id)
    if not restaurant:
        return {
            'id': None,
        }
    return {
        'id': restaurant.id,
        'name': restaurant.name,
        'tel': restaurant.tel,
        'address': restaurant.address,
        'gnavi_url': restaurant.gnavi_restaurant_url
    }
