from django.db import models
from .constraints import SourceType


class Restaurant(models.Model):

    restaurant_id = models.CharField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    name_kana = models.CharField(max_length=200, null=False, blank=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    category = models.CharField(max_length=200, null=False, blank=False)
    url = models.URLField()
    url_mobile = models.URLField()
    image_url_1 = models.URLField()
    image_url_2 = models.URLField()
    address = models.CharField(max_length=200, null=False, blank=False)
    tel = models.CharField(max_length=200, null=False, blank=False)
    tel_sub = models.CharField(max_length=200, null=True, blank=True)
    open_time = models.CharField(max_length=200, null=True, blank=True)
    holiday = models.CharField(max_length=200, null=True, blank=True)
    pr_short = models.CharField(max_length=500, null=True, blank=True)
    pr_long = models.TextField(null=True, blank=True)
    category_code_l = models.CharField(max_length=100, null=False, blank=False)
    category_name_l = models.CharField(max_length=100, null=False, blank=False)
    category_code_s = models.CharField(max_length=100, null=False, blank=False)
    category_name_s = models.CharField(max_length=100, null=False, blank=False)
    budget = models.CharField(max_length=300, null=True, blank=True)
    party = models.CharField(max_length=300, null=True, blank=True)
    lunch = models.CharField(max_length=300, null=True, blank=True)
    source_type = models.IntegerField(choices=SourceType.choices())

    class Meta:
        unique_together = ('restaurant_id', 'source_type')

    def __str__(self):
        return 'Restaurant({}, {})'.format(self.restaurant_id, self.name)