#!/usr/bin/env python3
""" This type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
