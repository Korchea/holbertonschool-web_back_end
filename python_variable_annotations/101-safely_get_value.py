#!/usr/bin/env python3
""" Add function’s parameters and return values with the appropriate types"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Add function’s parameters and return values with the
    appropriate types"""
    if key in dct:
        return dct[key]
    else:
        return default
