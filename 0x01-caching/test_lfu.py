#!/usr/bin/env python3
"""This script houses the LFU cache"""

from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """A class that inherits from BaseCaching and implements LFU cache"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.frequency = {}  # Dictionary to maintain access frequency of keys
        self.min_freq = 0  # Track the minimum frequency for efficient eviction

    def put(self, key, item):
        """Adds the item to the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                # If the key is already in the cache, update the item and its frequency
                self.cache_data[key] = item
                self.frequency[key] += 1
            else:
                # If the cache is full, evict the least frequently used item
                if len(self.cache_data) >= self.MAX_ITEMS:
                    # Find the least frequently used key(s)
                    min_freq_keys = [k for k, v in self.frequency.items() if v == self.min_freq]
                    lfu_key = min_freq_keys[0]  # Use the first one found (FIFO)
                    del self.cache_data[lfu_key]
                    del self.frequency[lfu_key]
                    print('DISCARD: {}'.format(lfu_key))

                # Add the new key to the cache
                self.cache_data[key] = item
                self.frequency[key] = 1
                self.min_freq = 1  # New key has the minimum frequency of 1

            # Update the minimum frequency if needed
            if self.frequency[key] == self.min_freq + 1:
                self.min_freq += 1
    
    def get(self, key):
        """ This method returns an item by the key and increments its frequency"""
        if key is None or key not in self.cache_data:
            return None
        # Increment the access frequency of the key
        self.frequency[key] += 1

        # Update the minimum frequency if necessary
        if self.frequency[key] == self.min_freq + 1:
            self.min_freq += 1

        return self.cache_data[key]
