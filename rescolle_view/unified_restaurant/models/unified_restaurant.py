from django.db import models


class UnifiedRestaurant(models.Model):

    name = models.CharField(max_length=400, null=False, blank=False)
    name_kana = models.CharField(max_length=400, null=False, blank=False)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    address = models.CharField(max_length=600, null=False, blank=False)
    tel = models.CharField(max_length=400, null=False, blank=False)
    gnavi_restaurant = models.ForeignKey('sns_restaurant.GnaviRestaurant', on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'UnifiedRestaurant({}: {})'.format(self.id, self.name)

    @classmethod
    def get_by_id(cls, restaurant_id):
        try:
            return cls.objects.get(id=restaurant_id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_by_gnavi_restaurant(cls, gnavi_restaurant):
        try:
            return cls.objects.get(gnavi_restaurant=gnavi_restaurant)
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_list_by_keyword(cls, keyword):
        return list(cls.objects.filter(gnavi_restaurant__pr_long__contains=keyword))

    @classmethod
    def get_all_valid_list(cls):
        return list(cls.objects.exclude(latitude=None, longitude=None))

    @classmethod
    def get_list_by_latlng(cls, north_east_lat, north_east_lng, south_west_lat, south_west_lng, limit=1000):
        """
        指定座標のすべてのリストを戻す
        :param north_east_lat:
        :param north_east_lng:
        :param south_west_lat:
        :param south_west_lng:
        :return:
        """
        query_set = cls.objects.filter(
            latitude__range=(south_west_lat, north_east_lat),
            longitude__range=(south_west_lng, north_east_lng),
        )[:1000]
        return list(query_set)


    @classmethod
    def get_list_by_id_list(cls, id_list):
        """
        :param list[int] id_list:
        :return:
        """
        return list(cls.objects.exclude(latitude=None, longitude=None).filter(id__in=id_list))

    @classmethod
    def get_list_by_id_list_with_coordinate(cls, id_list, north_east_lat, north_east_lng, south_west_lat, south_west_lng):
        """
        指定IDについて座標内のものを戻す
        :param id_list:
        :param north_east_lat:
        :param north_east_lng:
        :param south_west_lat:
        :param south_west_lng:
        :return:
        """
        query_set = cls.objects.filter(
            latitude__range=(south_west_lat, north_east_lat),
            longitude__range=(south_west_lng, north_east_lng),
        ).filter(id__in=id_list)
        return list(query_set)

    @property
    def gnavi_restaurant_url(self):
        return self.gnavi_restaurant.url
