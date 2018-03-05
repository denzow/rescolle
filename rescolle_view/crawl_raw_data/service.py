# coding: utf-8

from .models.crawl_raw_data import CrawlRawData


def get_crawled_data_by_serial(serial: str) -> CrawlRawData:
    return CrawlRawData.get_by_serial(serial)
