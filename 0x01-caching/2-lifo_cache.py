#!/usr/bin/python3
"""LIFO Caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Defines methods that implement LIFO caching"""

    def __init__(self):
        """Stores record of items removed from objects"""
        super().__init__()
        self.__removed = 0

    def put(self, key, item):
        """Stores an item in the cache"""

        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                if self.__removed == 0:
                    remove = list(self.cache_data.keys())[-2]
                    self.__removed = 1
                else:
                    remove = list(self.cache_data.keys())[-3]
                    self.__removed = 0
                self.cache_data.pop(remove)
                print(f"DISCARD: {remove}")

    def get(self, key):
        """Gets an item from the cache"""

        item = self.cache_data.get(key)
        return item
