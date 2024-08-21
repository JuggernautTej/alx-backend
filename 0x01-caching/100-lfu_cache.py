#!/usr/bin/env python3
"""This script houses the LFU cache"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A class that inherits from BaseCaching
    and implements LFU cache"""

    def __init__(self):
        """Initializes the class"""
        super().__init__()
        # Set up a dictionary to track access frequency of the keys
        self.frequency = {}
        # Set up the list to track order of keys for the
        # LRU when a tie is encountered
        self.access_order = []

    def put(self, key, item):
        """Adds the item to the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            # Update the item and it's frequency if it already exists
            self.cache_data[key] = item
            self.frequency[key] += 1
            # for the LRU part
            self.access_order.remove(key)
            self.access_order.append(key)
        else:
            # when the cache is full, the least frequently used item is deleted
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Find the keys with the minimum frequency
                min_freq = min(self.frequency.values())
                suspects = [k for k in self.cache_data if
                            self.frequency[k] == min_freq]

                # Remove the oldest key using LRU if there's a tie
                if len(suspects) > 1:
                    lfu_lru_key = next(k for k in self.access_order
                                       if k in suspects)
                else:
                    lfu_lru_key = suspects[0]
                # The eviction of the least frequently used key(LFU/LRU)
                del self.cache_data[lfu_lru_key]
                del self.frequency[lfu_lru_key]
                self.access_order.remove(lfu_lru_key)
                print('DISCARD: {}'.format(lfu_lru_key))
            # Add new key to the cache
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.access_order.append(key)

    def get(self, key):
        """This method returns an item by the key and
        increments its frequency"""
        if key is None or key not in self.cache_data:
            return None
        # Increment thhe access frequency of the key
        self.frequency[key] += 1
        # Update the access order for the LRU
        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]
