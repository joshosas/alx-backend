#!/usr/bin/env python3
"""Least Frequently Used (LFU) caching module.
"""
from collections import defaultdict

from datetime import datetime

from functools import total_ordering


class LFUCache(BaseCaching):
    """a class that allows storing, retreiving and
       and deleting (if cache is full) of information using
       the Least Recently Used (LFU) Replacement Policy.
    """

    def __init__(self):
        super().__init__()
        self.freq = defaultdict(int)
        self.last_used = {}
        self.access_count = 0

    def put(self, key, item):
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Find the least frequency used item(s)
            min_freq = min(self.freq.values())
            least_frequent_items = [
                key for key, value in self.freq.items() if value == min_freq
            ]

            if len(least_frequent_items) > 1:
                # If there are multiple least frequent items, use LRU algorithm
                least_recently_used_item = min(
                    least_frequent_items, key=lambda x: self.last_used[x]
                )
                del self.cache_data[least_recently_used_item]
                del self.freq[least_recently_used_item]
                del self.last_used[least_recently_used_item]
                print(f"DISCARD: {least_recently_used_item}")

            else:
                item_to_discard = least_frequent_items[0]
                del self.cache_data[item_to_discard]
                del self.freq[item_to_discard]
                del self.last_used[item_to_discard]
                print(f"DISCARD: {item_to_discard}")

            self.cache_data[key] = item
            self.freq[key] += 1
            self.last_used[key] = self.access_count
            self.access_count += 1

        def get(self, key):
            if key is None or key not in self.cache_data:
                return None

            self.freq[key] += 1
            self.last_used[key] = self.access_count
            self.access_count += 1

            return self.cache_data[key]
