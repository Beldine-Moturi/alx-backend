#!/usr/bin/env python3
"""Simple pagination"""
import csv
import math
from typing import List, Dict


index_range = __import__('0-simple_helper_function').index_range


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
        """returns indexes of a page"""

        assert (type(page) == int and type(page_size) == int),\
            "Values must be integers!"
        assert (page > 0 and page_size > 0), "Values must be greater than 0"

        start, end = index_range(page, page_size)
        if end > len(self.dataset()):
            return []
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Hypermedia generator """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        if self.__dataset:
            size = len(self.__dataset)
        else:
            size = 0
        dic = {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if page + 1 <= size else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': math.ceil(size / page_size),
        }
        return dic
