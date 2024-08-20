#!/usr/bin/python3
"""A class that inherits from BaseCaching and is
a caching system.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """This class inherits from BaseCaching"""

    def put(self, key, item):
        """Adds the item to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ This method returns an item by the key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
