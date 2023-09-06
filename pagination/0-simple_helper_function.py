#!/usr/bin/env python3
""" Write a function named index_range that takes two integer
arguments page and page_size.
The function should return a tuple of size two containing a start
index and an end index corresponding to the range of indexes to return
in a list for those particular pagination parameters."""


def index_range(page: int, page_size: int) -> tuple:
    """ Write a function named index_range that takes two integer
    arguments page and page_size.
    The function should return a tuple of size two containing a start
    index and an end index corresponding to the range of indexes to return
    in a list for those particular pagination parameters."""
    first = (page - 1) * page_size
    second = page * page_size
    return (first, second)
