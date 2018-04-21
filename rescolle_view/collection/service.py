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


def get_collection_data_by_owner_id(owner_id):
    """
    :param int owner_id:
    :return:
    :rtype: list[dict]
    """
    collection_list = Collection.get_list_by_owner_id(owner_id=owner_id)
    whole_dict = [collection.to_dict() for collection in collection_list]
    return whole_dict


def get_collection(collection_id):
    """
    :param int collection_id:
    :return:
    :rtype: Collection or None
    """
    return Collection.get_by_id(collection_id=collection_id)


def get_collected_restaurant_by_collection_id(collection_id):
    """
    :param int collection_id:
    :return:
    :rtype: list[CollectedRestaurant]
    """
    return CollectedRestaurant.get_list_by_collection_id(collection_id)
