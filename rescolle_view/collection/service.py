from .models import Collection, CollectedRestaurant


def create_collection(name, description, owner_id):
    """
    :param str name:
    :param str description:
    :param int owner_id:
    :return:
    """
    return Collection.create(
        owner_id=owner_id,
        description=description,
        name=name
    )


def add_restaurant_to_collection(collection_id, restaurant_id, memo):
    """
    :param int collection_id:
    :param int restaurant_id:
    :param str memo:
    :return:
    """
    collection = Collection.get_by_id(collection_id=collection_id)
    return CollectedRestaurant.create(
        collection=collection,
        restaurant_id=restaurant_id,
        memo=memo,
    )
