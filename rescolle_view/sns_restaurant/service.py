# coding: utf-8

from .generator import generate_gnavi_restaurant
from rescolle_view.unified_restaurant.unifier import get_unifier
from .constraints import SourceType


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
        print('unified', unified_restaurant.unify())


