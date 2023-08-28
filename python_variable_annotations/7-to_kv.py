#!/usr/bin/env python3
""" This type-annotated function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float."""
from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """ This type-annotated function sum_mixed_list which takes a list mxd_lst
    of integers and floats and returns their sum as a float."""
    return (k, v**2)
