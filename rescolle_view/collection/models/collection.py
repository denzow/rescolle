from django.db import models
from django.conf import settings


class Collection(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    order = models.IntegerField(default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Collection({}: {} of {})'.format(self.id, self.name, self.owner)

    @classmethod
    def create(cls, **params):
        return cls.objects.create(**params)

    @classmethod
    def get_by_id(cls, collection_id):
        try:
            return cls.objects.get(id=collection_id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_list_by_owner_id(cls, owner_id):
        return cls.objects.filter(owner_id=owner_id).order_by('order')

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'restaurants': [res.to_dict() for res in self.collectedrestaurant_set.all().order_by('order')]
        }
