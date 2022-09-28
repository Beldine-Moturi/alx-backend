#!/usr/bin/python3
"""Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""

    def put(self, key, item):
        """puts items in the cache"""

        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item from the chache"""

        item = self.cache_data.get(key)
        return key
