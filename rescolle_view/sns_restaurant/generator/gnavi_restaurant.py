# coding: utf-8
from rescolle_view.common import logger

from ..models.gnavi_restaurant import GnaviRestaurant


def generate_gnavi_restaurant(raw_dict_list: list):
    restaurant_list = []
    for raw_dict in raw_dict_list:
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

        if not parsed_data['latitude']:
            parsed_data['latitude'] = None
        else:
            # 以下を参考に座標を修正
            # http://oitake.jugem.jp/?eid=153
            latitude = float(parsed_data['latitude'])
            longitude = float(parsed_data['longitude'])
            parsed_data['latitude'] = latitude - latitude * 0.00010695 + longitude * 0.000017464 + 0.0046017

        if not parsed_data['longitude']:
            parsed_data['longitude'] = None
        else:
            latitude = float(parsed_data['latitude'])
            longitude = float(parsed_data['longitude'])
            parsed_data['longitude'] = longitude - latitude * 0.000046038 - longitude * 0.000083043 + 0.010040

        # for key in parsed_data.keys():
        #     if not parsed_data[key]:
        #         parsed_data[key] = ''

        instance = GnaviRestaurant.get_by_restaurant_id(restaurant_id=parsed_data['restaurant_id'])
        if instance:
            instance.update(**parsed_data)
            logger.debug('update {}'.format(instance))
        else:
            instance = GnaviRestaurant(**parsed_data)
            logger.debug('update {}'.format(instance))
        try:
            instance.save()
        except Exception as e:
            #logger.error('generate failed[{} {} {}]'.format(instance.longitude, instance.latitude, instance))
            from pprint import pprint
            pprint(parsed_data)
            raise e
        restaurant_list.append(instance)

    return restaurant_list
