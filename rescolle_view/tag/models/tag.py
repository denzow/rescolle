from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    related_tag = models.ManyToManyField('self')

    def __str__(self):
        return 'Tag({})'.format(self.name)

    @classmethod
    def get_by_name(cls, name):
        try:
            return cls.objects.get(name=name)
        except cls.DoesNotExist:
            return None

    @classmethod
    def create(cls, name):
        return cls.objects.create(name=name)
