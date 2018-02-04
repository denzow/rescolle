# -*- coding: utf-8 -*-

import os
import json
import requests

from .items import CrawlJsonItem


class RestaurantCollectorPipeline(object):

    def __init__(self, output_base_dir, request_endpoint):
        self.output_base_dir = output_base_dir
        self.request_endpoint = request_endpoint
        self.tmp_item_list = []

    @classmethod
    def from_crawler(cls, crawler):
        """
        :param crawler:
        :return:
        """
        return cls(
            output_base_dir=crawler.settings.get('GNAVI_RESTAURANT_OUTPUT_DATA_DIR'),
            request_endpoint=crawler.settings.get('RESCOLLE_SERVER_ENDPOINT'),
        )

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        crawl_json_item = CrawlJsonItem.create(self.tmp_item_list)
        crawl_json_item.save()

        # 生データの保存
        with open(os.path.join(self.output_base_dir, '{}.json'.format(spider.name)), 'w') as f:
            json.dump(self.tmp_item_list, f, indent=4, ensure_ascii=False)

        # 終了通知
        requests.get(self.request_endpoint + crawl_json_item['serial'])

    def process_item(self, item, spider):

        # print('{} {} {}'.format(item['name'], item['latitude'], item['longitude']))
        self.tmp_item_list.append(item)
        return item
