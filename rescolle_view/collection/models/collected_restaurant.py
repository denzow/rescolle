from django.db import models
from django.conf import settings


class CollectedRestaurant(models.Model):

    collection = models.ForeignKey('Collection', on_delete=models.CASCADE)
    restaurant = models.ForeignKey('unified_restaurant.UnifiedRestaurant', on_delete=models.CASCADE)
    memo = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return 'CollectedRestaurant({} in {})'.format(self.restaurant, self.collection)

    @classmethod
    def create(cls, **params):
        return cls.objects.create(**params)

    @classmethod
    def get_by_id(cls, collected_restaurant_id):
        try:
            return cls.objects.get(id=collected_restaurant_id)
        except cls.DoesNotExist:
            return None

    def to_dict(self):
        return {
            'restaurtant_id': self.restaurant_id,
            'restaurant_name': self.restaurant.name,
            'memo': self.memo,
        }