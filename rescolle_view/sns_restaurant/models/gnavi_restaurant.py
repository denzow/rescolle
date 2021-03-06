from django.db import models
from ..constraints import SourceType
from .abstract_sns_restaurant import AbstractSnsRestaurant


class GnaviRestaurant(models.Model, AbstractSnsRestaurant):

    restaurant_id = models.CharField(max_length=600, null=False, blank=False, unique=True)
    name = models.CharField(max_length=600, null=False, blank=False)
    name_kana = models.CharField(max_length=600, null=False, blank=False)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    category = models.CharField(max_length=600, null=False, blank=False)
    url = models.URLField()
    url_mobile = models.URLField()
    image_url_1 = models.URLField()
    image_url_2 = models.URLField()
    address = models.CharField(max_length=600, null=False, blank=False)
    tel = models.CharField(max_length=600, null=False, blank=False)
    tel_sub = models.CharField(max_length=600, null=True, blank=True)
    open_time = models.CharField(max_length=2000, null=True, blank=True)
    holiday = models.CharField(max_length=600, null=True, blank=True)
    pr_short = models.CharField(max_length=1000, null=True, blank=True)
    pr_long = models.TextField(null=True, blank=True)
    category_code_l = models.CharField(max_length=100, null=False, blank=False)
    category_name_l = models.CharField(max_length=100, null=False, blank=False)
    category_code_s = models.CharField(max_length=100, null=False, blank=False)
    category_name_s = models.CharField(max_length=100, null=False, blank=False)
    budget = models.CharField(max_length=300, null=True, blank=True)
    party = models.CharField(max_length=300, null=True, blank=True)
    lunch = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return 'GnaviRestaurant({}: {}, {})'.format(self.id, self.restaurant_id, self.name)

    @classmethod
    def get_by_restaurant_id(cls, restaurant_id):
        try:
            return cls.objects.get(restaurant_id=restaurant_id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_all_list(cls):
        return list(cls.objects.all())

    @classmethod
    def get_all_valid_list(cls):
        return list(cls.objects.exclude(latitude=-1, longitude=-1))

    @classmethod
    def get_list_by_keyword(cls, keyword):
        return list(cls.objects.filter(pr_long__contains=keyword))

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def source_type(self):
        return SourceType.GNAVI

    @property
    def image_url_list(self):
        image_url_list = []
        if self.image_url_1:
            image_url_list.append(self.image_url_1)
        if self.image_url_2:
            image_url_list.append(self.image_url_2)

        return image_url_list

    @property
    def description(self):
        if self.pr_long:
            return self.pr_long
        if self.pr_short:
            return self.pr_short
        return ''

    @property
    def description_text(self):
        return '{} {} {}'.format(
            self.pr_long,
            self.pr_short,
            self.name
        )


