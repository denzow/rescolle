# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import json

from scrapy_djangoitem import DjangoItem

from rescolle_view.constraints import SourceType
from rescolle_view.models import GnaviRestaurant, CrawlRawData


class CrawlJsonItem(DjangoItem):

    django_model = CrawlRawData

    @classmethod
    def create(cls, raw_dict_list: list):
        instance = cls()
        instance['raw_json'] = json.dumps(raw_dict_list)
        instance['source'] = SourceType.GNABI.value
        return instance


class RestaurantItem(DjangoItem):
    django_model = GnaviRestaurant

    @classmethod
    def create_by_dict(cls, raw_dict):
        code = raw_dict.get('code')
        parsed_data = {
            'restaurant_id': raw_dict.get('id'),
            'name': raw_dict.get('name'),
            'name_kana': raw_dict.get('name_kana'),
            'latitude': raw_dict.get('latitude'),
            'longitude': raw_dict.get('longitude'),
            'category': raw_dict.get('category'),
            'url': raw_dict.get('url'),
            'url_mobile': raw_dict.get('url_mobile'),
            'image_url_1': raw_dict.get('image_url').get('shop_image1'),
            'image_url_2': raw_dict.get('image_url').get('shop_image2'),
            'address': raw_dict.get('address'),
            'tel': raw_dict.get('tel'),
            'tel_sub': raw_dict.get('tel_sub'),
            'open_time': raw_dict.get('opentime'),
            'holiday': raw_dict.get('holiday'),
            'pr_short': raw_dict.get('pr').get('pr_short'),
            'pr_long': raw_dict.get('pr').get('pr_long'),
            'category_code_l': code.get('category_code_l')[0],
            'category_name_l': code.get('category_name_l')[0],
            'category_code_s': code.get('category_code_s')[0],
            'category_name_s': code.get('category_name_s')[0],
            'budget': raw_dict.get('budget'),
            'party': raw_dict.get('party'),
            'lunch': raw_dict.get('lunch'),
        }
        instance = cls(**parsed_data)
        if not instance['latitude']:
            instance['latitude'] = -1
        else:
            # 以下を参考に座標を修正
            # http://oitake.jugem.jp/?eid=153
            latitude = float(instance['latitude'])
            longitude = float(instance['longitude'])
            instance['latitude'] = latitude - latitude * 0.00010695 + longitude * 0.000017464 + 0.0046017
        if not instance['longitude']:
            instance['longitude'] = -1
        else:
            latitude = float(instance['latitude'])
            longitude = float(instance['longitude'])
            instance['longitude'] = longitude - latitude * 0.000046038 - longitude * 0.000083043 + 0.010040

        for key in instance.keys():
            if not instance[key]:
                instance[key] = ''

        return instance
