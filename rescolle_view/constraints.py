# coding: utf-8

import enum


class SourceType(enum.Enum):
    GNABI = 1

    @classmethod
    def choices(cls):
        return tuple([(m.value, m.name) for m in cls])
