# coding: utf-8

import json


class SmallArea:

    def __init__(self, small_area_name, small_area_code, middle_area_name,
                 middle_area_code, large_area_code, large_area_name, pref_name, pref_code):
        self.small_area_name = small_area_name
        self.small_area_code = small_area_code
        self.middle_area_name = middle_area_name
        self.middle_area_code = middle_area_code
        self.large_area_name = large_area_name
        self.large_area_code = large_area_code
        self.pref_name = pref_name
        self.pref_code = pref_code

    def __str__(self):
        return '{}({}:{})'.format(self.__class__.__name__, self.small_area_code, self.small_area_name)

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

    def __init__(self, json_data):
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
        self._raw_data = json.loads(json_data)
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
                small_area_name=area_dict['areaname_s'],
                small_area_code=area_dict['areacode_s'],
                middle_area_name=area_dict['garea_middle']['areaname_m'],
                middle_area_code=area_dict['garea_middle']['areacode_m'],
                large_area_name=area_dict['garea_large']['areaname_l'],
                large_area_code=area_dict['garea_large']['areacode_l'],
                pref_name=area_dict['pref']['pref_name'],
                pref_code=area_dict['pref']['pref_code'],
            )
            area_list.append(small_area)

        return area_list

    def search(self, **kwargs):
        """
        全部or条件
        :param kwargs: 検索条件のペア
        :return:
        """
        result_set = []
        for k, v in kwargs.items():
            for area in self._small_area_list:
                if area.is_match(k, v):
                    result_set.append(area)
        return result_set


if __name__ == '__main__':

    with open('./gnavi_area.json') as f:
        repo = GeoRepository(f.read())
        print(repo.search(middle_area_name='渋谷'))

