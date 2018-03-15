from django.db import models


class UnifiedRestaurant(models.Model):

    name = models.CharField(max_length=400, null=False, blank=False)
    name_kana = models.CharField(max_length=400, null=False, blank=False)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    address = models.CharField(max_length=600, null=False, blank=False)
    tel = models.CharField(max_length=400, null=False, blank=False)
    gnavi_restaurant = models.ForeignKey('sns_restaurant.GnaviRestaurant', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'UnifiedRestaurant({}: {})'.format(self.id, self.name)

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
        return list(cls.objects.exclude(latitude=-1, longitude=-1))

