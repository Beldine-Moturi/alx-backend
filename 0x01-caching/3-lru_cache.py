#!/usr/bin/python3
"""LRU Caching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Defines methods that implement LRU Caching"""

    def __init__(self):
        """Stores frequency of access for each value in the dictionary"""

        super().__init__()
        self.access = {}

    def put(self, key, item):
        """ Add an item in the cache
        """

        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # get the key with the lowest value in self.access
                lowest = min(self.access.values())
                keys = list(self.access.keys())
                l_key = keys[list(self.access.values()).index(lowest)]
                # remove that key-value pair from cache
                print(f"DISCARD: {l_key}")
                self.cache_data.pop(l_key)
                self.access.pop(l_key)
            self.cache_data[key] = item
            # add access frequency of this new item to self.access
            highest = max(self.access.values()) if self.access else 0
            self.access[key] = highest + 1

    def get(self, key):
        """Gets an item from the cache"""

        item = self.cache_data.get(key)
        # increase this item's access frequency in self.access
        if item:
            highest = max(self.access.values()) if self.access else 0
            self.access[key] = highest + 1
        return item
