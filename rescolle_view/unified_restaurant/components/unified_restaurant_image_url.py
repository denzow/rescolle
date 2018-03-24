from rescolle_view.common import logger
from ..models import UnifiedRestaurantImageUrl


def create_restaurant_images(restaurant, image_url_list):
    for image_url in image_url_list:
        try:
            UnifiedRestaurantImageUrl.create(
                restaurant=restaurant,
                image_url=image_url
            )
        except Exception as e:
            logger.error(e)


def get_url_list_by_restaurant(restaurant):
    images = UnifiedRestaurantImageUrl.get_list_by_restaurant_id(restaurant.id)
    return [image.image_url for image in images]
