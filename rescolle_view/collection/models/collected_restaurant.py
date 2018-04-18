from django.db import models
from django.conf import settings


class CollectedRestaurant(models.Model):

    collection = models.ForeignKey('Collection', on_delete=models.CASCADE)
    restaurant = models.ForeignKey('unified_restaurant.UnifiedRestaurant', on_delete=models.CASCADE)
    
    def __str__(self):
        return 'CollectedRestaurant({} in {})'.format(self.restaurant, self.collection)

    @classmethod
    def get_by_id(cls, collected_restaurant_id):
        try:
            return cls.objects.get(id=collected_restaurant_id)
        except cls.DoesNotExist:
            return None
