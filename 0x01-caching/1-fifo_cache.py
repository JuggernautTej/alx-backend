#!/usr/bin/env python3
"""This script houses the FIFO cache"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A class that inherits from BaseCaching"""
    def __init__(self):
        """Initializes the class"""
        super().__init__()
        self.key_order = []
    
    def put(self, key, item):
        """Adds the item to the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.key_order.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                oldest_key = self.key_order.pop(0)
                del self.cache_data[oldest_key]
                print('DISCARD: {}'.format(oldest_key))
            self.cache_data[key] = item
            self.key_order.append(key)
    
    def get(self, key):
        """ This method returns an item by the key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
