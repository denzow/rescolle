# coding: utf-8

import enum


class SourceType(enum.Enum):
    GNAVI = 1

    @classmethod
    def choices(cls):
        return tuple([(m.value, m.name) for m in cls])

    def is_gnavi(self):
        return self.value == self.GNAVI.value
