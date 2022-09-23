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
        """returns page indexes for a page"""

        dataset_size = len(self.dataset())
        data = self.get_page(page, page_size)
        total_pages = dataset_size / page_size
        if (dataset_size % page_size):
            total_pages += 1

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
