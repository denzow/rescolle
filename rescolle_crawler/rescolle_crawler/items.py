# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem

from rescolle_view.models import Restaurant
from rescolle_view.constraints import SourceType


class RestaurantItem(DjangoItem):
    django_model = Restaurant

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
            instance['latitude'] = float(instance['latitude']) + 0.00324
        if not instance['longitude']:
            instance['longitude'] = -1
        else:
            instance['longitude'] = float(instance['longitude']) - 0.0032

        for key in instance.keys():
            if not instance[key]:
                instance[key] = ''

        instance['source_type'] = SourceType.GNABI.value
        return instance
