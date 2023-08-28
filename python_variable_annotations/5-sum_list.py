#!/usr/bin/env python3
""" This type-annotated function sum_list which takes a list
input_list of floats as argument and returns their sum as a float."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ This type-annotated function sum_list which takes a list input_list
    of floats as argument and returns their sum as a float."""
    sum = 0.00
    for x in input_list:
        sum += x
    return sum
