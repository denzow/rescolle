# -*- coding: utf-8 -*-
import os
import json

import scrapy
from scrapy.http import Request, Response


from ..geo_repository import GeoRepository

# https://api.gnavi.co.jp/api/manual/restsearch/
# ぐるなびAPIでは現状1000以上を戻す検索では1000以降の結果をとれない制限がある
GNAVI_API_LIMIT = 1000


class GnaviShibuyaSpider(scrapy.Spider):

    name = 'gnavi_shibuya'
    allowed_domains = ['api.gnavi.co.jp']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # レストランサーチAPI
        self.api_url = 'https://api.gnavi.co.jp/RestSearchAPI/20150630/?offset_page={offset_page}&hit_per_page=100&format=json&keyid={api_key}&{areacode_type}={area_code}'
        self.gnavi_api_key = os.environ.get('GNAVI_API_KEY')
        # areacode_m 渋谷
        self.start_area_code = 'AREAM2126'
        self.start_area_type = 'areacode_m'
        # 大きいものが上位
        self.area_code_type_list = [
            'pref_code',
            'areacode_l',
            'areacode_m',
            'areacode_s',
        ]

    def _get_lower_area_code_type(self, base_type, change_level=0):
        """
        起点よりも細かいエリアのタイプ名を取得する
        :param str base_type: 起点のタイプ名
        :param int change_level: 1 なら1段階下
        :return: code type str
        :rtype: str
        """

        if base_type not in self.area_code_type_list:
            return None

        index = self.area_code_type_list.index(base_type)
        index += change_level
        if len(self.area_code_type_list) <= index:
            return None

        return self.area_code_type_list[index]

    def _get_api_url(self, area_code_type, area_code, offset_page=1):
        return self.api_url.format(
            api_key=self.gnavi_api_key,
            area_code=area_code,
            areacode_type=area_code_type,
            offset_page=offset_page
        )

    def _get_request(self, area_code_type, area_code, offset_page=1, callback_parser=None):
        """
        Metaに必要な情報を保持したリクエストを戻す
        :param area_code_type:
        :param area_code:
        :param offset_page:
        :param callback_parser:
        :return:
        """

        if not callback_parser:
            callback_parser = self.parse
        search_pattern = {
            'area_code_type': area_code_type,
            'area_code': area_code,
            'offset_page': offset_page
        }

        target_url = self._get_api_url(**search_pattern)
        request = Request(url=target_url, callback=callback_parser)
        request.meta['search_pattern'] = search_pattern
        return request

    def start_requests(self):
        """
        ここから始まる
        :return:
        """

        yield self._get_request(
            offset_page=1,
            area_code_type=self.start_area_type,
            area_code=self.start_area_code,
            callback_parser=self.parse
        )

    def parse(self, response):
        """
        ぐるなびサーチAPIの結果を解析する
        :param Response response:
        :return:
        """

        result = json.loads(response.body)
        search_pattern = response.meta['search_pattern']

        # 上限超過等、エラーがでたらやめる
        if 'error' in result:
            self.logger.error(result)
            return

        total_hit_count = int(result['total_hit_count'])
        # 検索条件超過の場合はエリアを狭める
        if total_hit_count > GNAVI_API_LIMIT:
            one_point_down_code_type = self._get_lower_area_code_type(search_pattern['area_code_type'], 1)

            # エリアリポジトリからもともとのエリアを細分化した小エリアを取得する
            sub_area_code_list = GeoRepository().search(**{
                'select': one_point_down_code_type,
                search_pattern['area_code_type']: search_pattern['area_code']
            })

            # 各サブコードごとに再帰リクエストを投げる
            for sub_area_code in sub_area_code_list:
                search_pattern['area_code_type'] = one_point_down_code_type
                search_pattern['area_code'] = sub_area_code

                yield self._get_request(**search_pattern, callback_parser=self.parse)

        else:
            hit_per_page = int(result['hit_per_page'])
            page_offset = int(result['page_offset'])

            self.logger.info('################# {}/{}'.format(hit_per_page * page_offset, total_hit_count))

            # 結果をItemPipelineに流す
            for rest in result['rest']:
                yield rest

            # まだ全件戻ってないならOffsetをずらして続ける
            if hit_per_page * page_offset < total_hit_count:
                search_pattern['offset_page'] += 1
                yield self._get_request(**search_pattern, callback_parser=self.parse)


