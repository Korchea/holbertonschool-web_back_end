#!/usr/bin/env python3
""" Implement a get_hyper method that takes the same arguments
(and defaults) as get_page and returns a dictionary containing
the following key-value pairs"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """ Write a function named index_range that takes two integer
    arguments page and page_size.
    The function should return a tuple of size two containing a start
    index and an end index corresponding to the range of indexes to return
    in a list for those particular pagination parameters."""
    first = (page - 1) * page_size
    second = page * page_size
    return (first, second)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Implement a method named get_page that takes two integer arguments
        page with default value 1 and page_size with default value 10."""
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0
        result = index_range(page, page_size)
        self.dataset()
        return self.__dataset[result[0]: result[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ Implement a get_hyper method that takes the same arguments
        (and defaults) as get_page and returns a dictionary containing
        the following key-value pairs"""
        total_pages: int = len(self.dataset())
        if page > total_pages:
            next_page = None
        else:
            next_page = page + 1
        if page < 1:
            prev_page = None
        else:
            prev_page = page - 1
        dict_data = {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
        return dict_data
