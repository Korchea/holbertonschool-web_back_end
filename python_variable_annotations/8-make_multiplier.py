#!/usr/bin/env python3
""" This type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ This type-annotated function make_multiplier that takes a float
    multiplier as argument and returns a function that multiplies a
    float by multiplier."""
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
