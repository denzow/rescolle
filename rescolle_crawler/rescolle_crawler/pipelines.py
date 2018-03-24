# -*- coding: utf-8 -*-

import os
import json
import requests

from .items import CrawlJsonItem


class RestaurantCollectorPipeline:

    def __init__(self, request_endpoint):
        self.request_endpoint = request_endpoint
        self.tmp_item_list = []

    @classmethod
    def from_crawler(cls, crawler):
        """
        :param crawler:
        :return:
        """
        return cls(
            request_endpoint=crawler.settings.get('RESCOLLE_SERVER_ENDPOINT'),
        )

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        """
        item単位で処理はせず、貯めるだけにしている
        :param item:
        :param spider:
        :return:
        """
        self.tmp_item_list.append(item)
        return item

    def close_spider(self, spider):
        crawl_json_item = CrawlJsonItem.create(self.tmp_item_list)
        crawl_json_item.save()
        # 終了通知
        spider.logger.info('send finish message for {}'.format(crawl_json_item['serial']))
        requests.get(self.request_endpoint + crawl_json_item['serial'])
