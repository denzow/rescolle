from django.db import models


class UnifiedRestaurantImageUrl(models.Model):

    restaurant = models.ForeignKey('UnifiedRestaurant', on_delete=models.CASCADE)
    image_url = models.URLField()

    class Meta:
        unique_together = ('restaurant', 'image_url')

    @classmethod
    def create(cls, restaurant, image_url):
        return cls.objects.create(restaurant=restaurant, image_url=image_url)

    @classmethod
    def get_list_by_restaurant_id(cls, restaurant_id):
        return list(cls.objects.filter(restaurant_id=restaurant_id))
