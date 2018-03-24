from ..constraints import SourceType


class AbstractSnsRestaurant:

    @property
    def source_type(self):
        """
        :return:
        :rtype: SourceType
        """
        raise NotImplementedError('not implemented')

    @property
    def image_url_list(self):
        """
        :return:
        :rtype: list[str]
        """
        raise NotImplementedError('not implemented')

    @property
    def description_text(self):
        """
        :return:
        :rtype: str
        """
        raise NotImplementedError('not implemented')

