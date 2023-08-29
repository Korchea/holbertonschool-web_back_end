#!/usr/bin/env python3
""" Add function’s parameters and return values with the appropriate types"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Add function’s parameters and return values with the
    appropriate types"""
    if lst:
        return lst[0]
    else:
        return None
