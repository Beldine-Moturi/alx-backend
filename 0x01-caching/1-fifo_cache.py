#!/usr/bin/python3
"""FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """defines methods that implement FIFO caching"""

    def put(self, key, item):
        """Stores an item in the cache"""

        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                first_item = next(iter(self.cache_data))
                self.cache_data.pop(first_item)
                print(f"DISCARD: {first_item}")

    def get(self, key):
        """Gets an item from the cache"""

        super().get()
