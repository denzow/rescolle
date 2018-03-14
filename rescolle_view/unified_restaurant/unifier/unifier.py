# coding: utf-8

import abc

from rescolle_view.common.exceptions import RescolleExceptions
from ..models.unified_restaurant import UnifiedRestaurant
from rescolle_view.sns_restaurant.constraints import SourceType
from rescolle_view.tag import service as tag_sv

def get_unifier(source_type: SourceType):

    unifier_map = {
        source_type.GNAVI: GnaviUnifier
    }

    return unifier_map[source_type]


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

    def _get_or_create_unified_restaurant(self, unify_target):
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
            if source_type.is_gnavi():
                ur = UnifiedRestaurant.get_by_gnavi_restaurant(gnavi_restaurant=target)
            # TODO 増える
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
            ur = UnifiedRestaurant()
            ur.save()
            return ur

    def unify(self):
        """
        複数のソースを統合する
        :return:
        """
        # unify可能なサブレストランを取得する
        # source_typeをキーとしてサブレストランをValueに持つ
        unify_target = self._get_unify_target()
        # 起点となるレストランを候補に加える
        unify_target[self.source_type] = self.source_object

        target_unified_restaurant = self._get_or_create_unified_restaurant(unify_target)

        # Unify時のソースの優先度順に並べる
        # TODO ソースの優先順位の決定
        sorted_source_keys = sorted(unify_target.keys(), key=lambda x: x.value)

        target_unified_restaurant.name = self._get_best_attribute('name', unify_target, sorted_source_keys)
        target_unified_restaurant.name_kana = self._get_best_attribute('name_kana', unify_target, sorted_source_keys)
        target_unified_restaurant.latitude = self._get_best_attribute('latitude', unify_target, sorted_source_keys)
        target_unified_restaurant.longitude = self._get_best_attribute('longitude', unify_target, sorted_source_keys)
        target_unified_restaurant.address = self._get_best_attribute('address', unify_target, sorted_source_keys)
        target_unified_restaurant.tel = self._get_best_attribute('tel', unify_target, sorted_source_keys)

        restaurant_description_text = ' '.join(self._get_total_attribute('pr_short', unify_target)) + \
                                      ' '.join(self._get_total_attribute('pr_long', unify_target))

        self._set_tag_level(restaurant_description_text, target_unified_restaurant.id)

        # TODO 今後増える
        target_unified_restaurant.gnavi_restaurant = unify_target.get(SourceType.GNAVI)

        target_unified_restaurant.save()
        return target_unified_restaurant

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

    def _get_total_attribute(self, attr_name, source_dict):
        """
        指定した属性について全て取得する
        :param attr_name:
        :param dict source_dict:
        :return:
        :rtype: list
        """
        result_list = []
        for key, restaurant in source_dict.items():
            result_list.append(getattr(restaurant, attr_name, ''))

        return result_list

    def _set_tag_level(self, description, restaurant_id):
        """
        レストランにタグレベルをセットする。毎回一回消す
        :param description:
        :param restaurant_id:
        :return:
        """
        tag_sv.clear_tag_level(restaurant_id)
        tag_sv.set_tag_level_to_restaurant(base_str=description, restaurant_id=restaurant_id)

    @staticmethod
    def _is_gnavi_restaurant(target):
        return target.source_type.is_gnavi()

    def _is_unify_able(self, candidate):
        """
        統合可能かの判定
        TODO
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
