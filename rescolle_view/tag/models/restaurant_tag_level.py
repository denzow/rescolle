from django.db import models


class RestaurantTagLevel(models.Model):

    restaurant = models.ForeignKey('unified_restaurant.UnifiedRestaurant', on_delete=models.CASCADE)
    tag = models.ForeignKey('tag.Tag', on_delete=models.CASCADE)
    level = models.FloatField(null=False, blank=False)

    def __str__(self):
        return 'RestaurantTagLevel({}:{}:{})'.format(self.restaurant.name, self.tag, self.level)

    @classmethod
    def create(cls, *args, **kwargs):
        return cls.objects.create(*args, **kwargs)

    @classmethod
    def delete_by_restaurant_id(cls, restaurant_id):
        cls.objects.filter(restaurant_id=restaurant_id).delete()

    @classmethod
    def get_list_by_tag_keyword(cls, keyword):
        return list(cls.objects.filter(tag__name__contains=keyword))
