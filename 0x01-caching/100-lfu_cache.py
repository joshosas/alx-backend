#!/usr/bin/env python3
"""Least Frequencyuently Used (LFU) caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """a class that allows storing, retreiving and
       and deleting (if cache is full) of information using
       the Least Recently Used (LFU) Replacement Policy.
    """

    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_frequency = []

    def __reorder_items(self, mru_key):
        """Reorders all items in the cache in order most
        recently used item.
        """
        max_positions = []
        mru_frequency = 0
        mru_pos = 0
        ins_pos = 0
        for i, key_frequency in enumerate(self.keys_frequency):
            if key_frequency[0] == mru_key:
                mru_frequency = key_frequency[1] + 1
                mru_pos = i
                break
            elif len(max_positions) == 0:
                max_positions.append(i)
            elif key_frequency[1] < self.keys_frequency[max_positions[-1]][1]:
                max_positions.append(i)
        max_positions.reverse()
        for pos in max_positions:
            if self.keys_frequency[pos][1] > mru_frequency:
                break
            ins_pos = pos
        self.keys_frequency.pop(mru_pos)
        self.keys_frequency.insert(ins_pos, [mru_key, mru_frequency])

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_frequency[-1]
                self.cache_data.pop(lfu_key)
                self.keys_frequency.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.keys_frequency)
            for i, key_frequency in enumerate(self.keys_frequency):
                if key_frequency[1] == 0:
                    ins_index = i
                    break
            self.keys_frequency.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
