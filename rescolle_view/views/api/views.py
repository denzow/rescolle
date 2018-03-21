import threading
from django.shortcuts import render
from django.http import JsonResponse

from rescolle_view.unified_restaurant import service as ur_sv
from rescolle_view.sns_restaurant import service as sns_res_sv
from rescolle_view.crawl_raw_data import service as raw_sv
from rescolle_view.common import logger


def get_restaurant(request, restaurant_id):
    """
    特定レストランの情報を戻す
    :param request:
    :param restaurant_id:
    :return:
    """
    info = ur_sv.get_restaurant_info(restaurant_id)
    return JsonResponse({
        'restaurant': info
    })


def get_coordinate_list(request):

    keyword = request.POST.get('keyword')
    north_east_lat = float(request.POST.get('north_east_lat'))
    north_east_lng = float(request.POST.get('north_east_lng'))
    south_west_lat = float(request.POST.get('south_west_lat'))
    south_west_lng = float(request.POST.get('south_west_lng'))
    if keyword:
        restaurant_coordinate_list = ur_sv.get_restaurant_coordinate_list_by_keyword(
            keyword=keyword,
            north_east_lat=north_east_lat + 0.005,
            north_east_lng=north_east_lng + 0.005,
            south_west_lat=south_west_lat - 0.005,
            south_west_lng=south_west_lng - 0.005,
        )
    else:
        restaurant_coordinate_list = ur_sv.get_all_restaurant_coordinate_list()

    return JsonResponse({
        'restaurants': restaurant_coordinate_list,
        'center': ur_sv.get_center_position(restaurant_coordinate_list),
    })


def generate_restaurant_endpoint(request, json_serial):
    """
    クローラから叩かれるエンドポイント
    JSONをもとに対応するレストランを生成する
    :param request:
    :param json_serial:
    :return:
    """

    def _async(target_crawled_data):
        logger.info('generate run')
        sns_res_sv.generate_restaurant_data(target_crawled_data.json, target_crawled_data.source_type)
        target_crawled_data.clear_serial()

    crawled_data = raw_sv.get_crawled_data_by_serial(serial=json_serial)
    if crawled_data:
        thread = threading.Thread(target=_async, args=(crawled_data, ))
        thread.start()
        logger.info('generate run')

        return JsonResponse({
            'status': 'end',
            'error': '',
        })
    else:
        return JsonResponse({
            'status': 'end',
            'error': 'invalid serial.'
        })
