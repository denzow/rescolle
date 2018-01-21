# coding: utf-8

import json
from scrapy.utils.project import get_project_settings

class SmallArea:

    def __init__(self, areaname_s, areacode_s, areaname_m, areacode_m, areaname_l, areacode_l, pref_name, pref_code):
        self.areaname_s = areaname_s
        self.areacode_s = areacode_s
        self.areaname_m = areaname_m
        self.areacode_m = areacode_m
        self.areaname_l = areaname_l
        self.areacode_l = areacode_l
        self.pref_name = pref_name
        self.pref_code = pref_code

    def __str__(self):
        return '{}({}:{})'.format(self.__class__.__name__, self.areacode_s, self.areaname_s)

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, key):
        return getattr(self, key)

    def get(self, key, default=None):
        try:
            return getattr(self, key)
        except AttributeError:
            return default

    def is_match(self, attr_name, value):
        return self.get(attr_name) == value


class GeoRepository:

    def __init__(self):
        """

        :param str json_data:
        """
        """
        {
            "@attributes": {
                "api_version": "20150630"
            },
            "garea_small": [
                {
                    "areacode_s": "AREAS5502",
                    "areaname_s": "札幌駅",
                    "garea_middle": {
                        "areacode_m": "AREAM5502",
                        "areaname_m": "札幌駅"
                    },
                    "garea_large": {
                        "areacode_l": "AREAL5500",
                        "areaname_l": "札幌駅・大通・すすきの"
                    },
                    "pref": {
                        "pref_code": "PREF01",
                        "pref_name": "北海道"
                    }
                },
        :
        """
        geo_file_path = get_project_settings().get('GNAVI_AREA_JSON_PATH')
        with open(geo_file_path) as f:
            self._raw_data = json.loads(f.read())
        self._small_area_list = self._prepare_repository()

    def _prepare_repository(self):
        """
        JSONをもう少しまともにする
        :return:
        :rtype: list[SmallArea]
        """

        small_area_list = self._raw_data['garea_small']
        area_list = []
        for area_dict in small_area_list:
            small_area = SmallArea(
                areaname_s=area_dict['areaname_s'],
                areacode_s=area_dict['areacode_s'],
                areaname_m=area_dict['garea_middle']['areaname_m'],
                areacode_m=area_dict['garea_middle']['areacode_m'],
                areaname_l=area_dict['garea_large']['areaname_l'],
                areacode_l=area_dict['garea_large']['areacode_l'],
                pref_name=area_dict['pref']['pref_name'],
                pref_code=area_dict['pref']['pref_code'],
            )
            area_list.append(small_area)

        return area_list

    def search(self, select, **kwargs):
        """
        全部or条件
        :param select: SELECT句
        :param kwargs: 検索条件のペア
        :return:
        """
        result_set = []
        for k, v in kwargs.items():
            for area in self._small_area_list:
                if area.is_match(k, v):
                    result_set.append(area[select])
        return list(set(result_set))


if __name__ == '__main__':

    with open('./gnavi_area.json') as f:
        repo = GeoRepository(f.read())
        print(repo.search('pref_name', areaname_m='渋谷'))
        print(repo.search('areaname_s', areaname_m='渋谷'))

