from itertools import chain


def flatten(target_list: list) -> list:
    return list(chain.from_iterable(target_list))
