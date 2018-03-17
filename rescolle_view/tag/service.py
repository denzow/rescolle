# coding: utf-8

from collections import Counter

from .tag import Tokenizer
from .models import Tag, RestaurantTagLevel
from .constants import OPERATOR


def generate_tags(base_str: str) -> list:
    """
    ある文章から名詞表現だけを取得し、Tgaを生成する
    :param base_str:
    :return:
    """
    tag_list = []
    tokenizer = Tokenizer()
    token_list = tokenizer.get_tokens(base_str)
    for token in token_list:
        tag = Tag.get_by_name(name=token['surface'])
        if not tag:
            tag = Tag.create(name=token['surface'])
        tag_list.append(tag)
    return tag_list


def clear_tag_level(restaurant_id: int) -> None:
    """
    レストランにセットされているタグを解除する
    :param restaurant_id:
    :return:
    """
    RestaurantTagLevel.delete_by_restaurant_id(restaurant_id=restaurant_id)


def set_tag_level_to_restaurant(base_str: str, restaurant_id: int) -> list:
    """
    レストランにタグを追加する
    :param base_str: タグ生成元になる文章
    :param restaurant_id: 対象のレストランID
    :return:
    """
    tag_list = generate_tags(base_str)
    counted_tag = Counter(tag_list)
    total_count = len(counted_tag.keys())
    tag_level_list = []
    for tag, count in counted_tag.items():
        level = round(count/total_count, 3)
        tag_level = RestaurantTagLevel.create(**{
            'tag': tag,
            'level': level,
            'restaurant_id': restaurant_id
        })
        tag_level_list.append(tag_level)

    return tag_level_list


def get_restaurant_by_tag_keyword(keyword: str, operator=OPERATOR.AND, filter_level=0) -> list:
    """
    指定したタグを持つレストランIDを戻す。
    フリーワードは一旦トークナイズしてから複数タグでのマッチングをする
    :param keyword:
    :param operator:
    :param filter_level:
    :return:
    """
    tokenizer = Tokenizer()
    words = tokenizer.get_token_text_list(keyword)
    result_id_list = []
    for word in words:
        tag_level_list = RestaurantTagLevel.get_list_by_tag_keyword(word)
        restaurant_id_list = [r.restaurant_id for r in tag_level_list if r.level > filter_level]

        if result_id_list:
            if operator == OPERATOR.AND:
                result_id_list = list(set(restaurant_id_list) & set(restaurant_id_list))
            elif operator == OPERATOR.OR:
                result_id_list = list(set(restaurant_id_list) | set(restaurant_id_list))
        else:
            result_id_list = restaurant_id_list

    return result_id_list
