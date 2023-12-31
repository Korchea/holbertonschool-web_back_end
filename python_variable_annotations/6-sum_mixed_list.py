#!/usr/bin/env python3
""" This type-annotated function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ This type-annotated function sum_mixed_list which takes a list mxd_lst
    of integers and floats and returns their sum as a float."""
    sum = 0.00
    for x in mxd_lst:
        sum += x
    return sum
