# coding: utf-8

import abc

from ..models import GnaviRestaurant, UnifiedRestaurant
from ..constraints import SourceType
from ..exceptions import RescolleExceptions


class UnifyExceptions(RescolleExceptions):
    """
    unify時の例外
    """


class Unifier(abc.ABC):

    def __init__(self, source_object):
        """

        :param source_object:
        """
        self.source_object = source_object
        self.source_type = None

    @abc.abstractmethod
    def _get_candidates_map(self):
        """
        CandidateMapを埋める。起点になるModelごとに埋め方は違うので
        サブクラスで実装される。
        :return:
        :rtype: dict
        """

    def _get_unify_target(self):
        """
        unify対象のモデル群を取得する
        {
            SourceType.GNAVI: TargetModel
            :
        }
        :return:
        :rtype: dict
        """
        unify_target = {}
        for source_type, candidate_list in self._get_candidates_map():
            for candidate in candidate_list:
                if self._is_unify_able(candidate):
                    unify_target[source_type] = candidate
                    break

        return unify_target

    def _get_unified_restaurant(self, unify_target):
        """
        すでに紐付いているUnifiedRestaurantがあれば戻す。
        なければ生成して戻す
        :param dict unify_target:
        :return:
        :rtype: UnifiedRestaurant
        """
        ur_list = []
        for source_type, target in unify_target.items():
            ur = None
            if source_type.is_gnavi:
                ur = UnifiedRestaurant.get_by_gnavi_restaurant(gnavi_restaurant=target)
            else:
                pass
            if ur:
                ur_list.append(ur)

        # 通常2個以上のURが同じサブレストランからあってはいけない
        if len(ur_list) > 1:
            raise UnifyExceptions('unexpected UnifiedRestaurant exist [{}]'.format(','.join(ur_list)))

        if ur_list:
            return ur_list[0]
        else:
            return UnifiedRestaurant()

    def unify(self):
        """
        複数のソースを統合する
        :return:
        """
        unify_target = self._get_unify_target()
        # 起点を候補に加える
        unify_target[self.source_type] = self.source_object
        target_unified_restaurant = self._get_unified_restaurant(unify_target)
        sorted_source_keys = sorted(unify_target.keys(), key=lambda x: x.value)

        target_unified_restaurant.name = self._get_best_attribute('name', unify_target, sorted_source_keys)
        target_unified_restaurant.name_kana = self._get_best_attribute('name_kana', unify_target, sorted_source_keys)
        target_unified_restaurant.latitude = self._get_best_attribute('latitude', unify_target, sorted_source_keys)
        target_unified_restaurant.longitude = self._get_best_attribute('longitude', unify_target, sorted_source_keys)
        target_unified_restaurant.address = self._get_best_attribute('address', unify_target, sorted_source_keys)
        target_unified_restaurant.tel = self._get_best_attribute('tel', unify_target, sorted_source_keys)
        target_unified_restaurant.gnavi_restaurant = unify_target.get(SourceType.GNAVI)

        target_unified_restaurant.save()

    def _get_best_attribute(self, attr_name, source_dict, priority_source_key_list):
        """
        候補の中でもっとも有意な値を戻す
        :param attr_name:
        :return:
        """
        for source_key in priority_source_key_list:
            restaurant = source_dict.get(source_key)
            if restaurant and getattr(restaurant, attr_name):
                return getattr(restaurant, attr_name)

        return None

    @staticmethod
    def _is_gnavi_restaurant(target):
        return isinstance(target, GnaviRestaurant)

    def _is_unify_able(self, candidate):
        """
        統合可能か
        :return:
        """
        longitude = self.source_object.longitude
        latitude = self.source_object.latitude
        return False


class GnaviUnifier(Unifier):

    def __init__(self, source_object):
        super().__init__(source_object)
        self.source_type = SourceType.GNAVI

    def _get_candidates_map(self):
        """
        現時点ではぐるなびしかクロールしてないので何も統合されない
        :return:
        """
        return {}
