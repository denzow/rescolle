import threading
from django.shortcuts import render
from django.http import JsonResponse

from rescolle_view.sns_restaurant import service as sns_res_sv
from rescolle_view.crawl_raw_data import service as raw_sv


def index(request):
    return render(request, 'index.html')

#
# def get_coordinate_list(request):
#
#     keyword = request.GET.get('keyword')
#     if keyword:
#         restaurant_coordinate_list = get_restaurant_coordinate_list_by_keyword(keyword)
#     else:
#         restaurant_coordinate_list = get_all_restaurant_coordinate_list()
#
#     return JsonResponse({
#         'restaurants': restaurant_coordinate_list,
#         'center': get_center_position(restaurant_coordinate_list),
#     })


def generate_restaurant_endpoint(request, json_serial):
    """
    クローラから叩かれるエンドポイント
    JSONをもとに対応するレストランを生成する
    :param request:
    :param json_serial:
    :return:
    """
    def _async(target_crawled_data):
        sns_res_sv.generate_restaurant_data(crawled_data.json, target_crawled_data.source_type)
        target_crawled_data.clear_serial()

    crawled_data = raw_sv.get_crawled_data_by_serial(serial=json_serial)
    if crawled_data:
        threading.Thread(target=_async, args=(crawled_data, ))
        return JsonResponse({
            'status': 'end',
            'error': '',
        })
    else:
        return JsonResponse({
            'status': 'end',
            'error': 'invalid serial.'
        })
