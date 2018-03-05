# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import json
import uuid

from scrapy_djangoitem import DjangoItem

from rescolle_view.sns_restaurant.constraints import SourceType
from rescolle_view.crawl_raw_data.models import CrawlRawData


class CrawlJsonItem(DjangoItem):

    django_model = CrawlRawData

    @classmethod
    def create(cls, raw_dict_list: list):
        instance = cls()
        instance['raw_json'] = json.dumps(raw_dict_list)
        instance['source'] = SourceType.GNAVI.value
        instance['serial'] = str(uuid.uuid1()).replace('-', '')
        return instance
