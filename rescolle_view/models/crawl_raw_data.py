import json

from django.db import models
from ..constraints import SourceType


class CrawlRawData(models.Model):

    raw_json = models.TextField()
    source = models.IntegerField()
    crawled_at = models.DateTimeField(auto_now_add=True)
    serial = models.TextField(blank=True, null=True, unique=True)

    @classmethod
    def get_by_serial(cls, serial):
        try:
            return cls.objects.get(serial=serial)
        except cls.DoesNotExist:
            return None

    @property
    def json(self):
        return json.loads(self.raw_json)

    @property
    def source_type(self):
        return SourceType(self.source)

    def clear_serial(self):
        self.serial = None
        self.save()
