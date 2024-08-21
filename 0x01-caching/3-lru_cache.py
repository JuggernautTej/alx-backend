#!/usr/bin/env python3
"""This script houses the LRU cache"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A class that inherits from BaseCaching and implements the LRU cache"""
    def __init__(self):
        """Initializes the class"""
        super().__init__()
        # The list to track the access order for the LRU
        self.access_order = []

    def put(self, key, item):
        """Adds the item to the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                # If key is already in the cache, it's position is updated
                self.access_order.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                # If the cache is full, the least recently used item is removed
                lru_key = self.access_order.pop(0)
                del self.cache_data[lru_key]
                print('DISCARD: {}'.format(lru_key))
            self.cache_data[key] = item
            self.access_order.append(key)

    def get(self, key):
        """ This method returns an item by the key and
        marks it as recently used"""
        if key is None or key not in self.cache_data:
            return None
        # Mark the key as recently used by moving it to the end of access_order
        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]
