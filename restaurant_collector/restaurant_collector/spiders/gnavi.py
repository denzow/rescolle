# -*- coding: utf-8 -*-
import os
import json

import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup

# https://api.gnavi.co.jp/api/manual/restsearch/


class GnaviSpider(scrapy.Spider):
    name = 'gnavi'
    allowed_domains = ['api.gnavi.co.jp']
    api_url = 'https://api.gnavi.co.jp/RestSearchAPI/20150630/?offset_page={offset_page}&hit_per_page=100&format=json&keyid={api_key}&areacode_m={area_code}'
    gnavi_api_key = os.environ.get('GNAVI_API_KEY')
    shibuya_code = 'AREAM2126'
    offset_page = 1

    def _get_api_url(self, offset_page=1):
        return self.api_url.format(
            api_key=self.gnavi_api_key,
            area_code=self.shibuya_code,
            offset_page=offset_page
        )

    def start_requests(self):
        yield Request(self._get_api_url(offset_page=self.offset_page), self.parse_json)

    def parse_json(self, response):

        result = json.loads(response.body)

        # 上限超過等、エラーがでたらやめる
        if 'error' in result:
            print(result)
            return

        total_hit_count = int(result['total_hit_count'])
        hit_per_page = int(result['hit_per_page'])
        page_offset = int(result['page_offset'])
        self.logger.info('################# {}/{}'.format(hit_per_page * page_offset, total_hit_count))

        for rest in result['rest']:
            self.logger.debug('{} {} {}'.format(rest['name'], rest['latitude'], rest['longitude']))
            yield rest

        if hit_per_page * page_offset < total_hit_count:
            self.offset_page += 1
            yield Request(self._get_api_url(offset_page=self.offset_page), self.parse_json)
