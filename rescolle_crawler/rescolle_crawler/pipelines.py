# -*- coding: utf-8 -*-

import os
import json

from .items import RestaurantItem

class RestaurantCollectorPipeline(object):

    def __init__(self, output_base_dir):
        self.output_base_dir = output_base_dir
        self.tmp_item_list = []

    @classmethod
    def from_crawler(cls, crawler):
        """
        :param crawler:
        :return:
        """
        return cls(
            output_base_dir=crawler.settings.get('GNAVI_RESTAURANT_OUTPUT_DATA_DIR')
        )

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):

        # 生データの保存
        with open(os.path.join(self.output_base_dir, '{}.json'.format(spider.name)), 'w') as f:
            json.dump(self.tmp_item_list, f, indent=4, ensure_ascii=False)

        for data in self.tmp_item_list:
            restaurant = RestaurantItem.create_by_dict(data)
            print(restaurant)
            restaurant.save()

    def process_item(self, item, spider):

        # print('{} {} {}'.format(item['name'], item['latitude'], item['longitude']))
        self.tmp_item_list.append(item)
        return item