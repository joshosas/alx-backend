#!/usr/bin/env python3
"""Basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """a class that allows storing and retreiving
       information in a dictionary.
    """

    def put(self, key, item):
        """Store an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
