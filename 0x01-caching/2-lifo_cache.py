#!/usr/bin/env python3
""" BaseCaching module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Defines a class for caching information using LIFO strategy
    Methods:
        put(key, item) - store a key-value pair
        get(key) - retrieve the value associated with a key
    """
    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Store a key-value pair"""
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= self.MAX_ITEMS and\
              key not in self.cache_data:
                print("DISCARD: {}".format(self.order[-1]))
                del self.cache_data[self.order[-1]]
                del self.order[-1]
            if key in self.order:
                del self.order[self.order.index(key)]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Return value linked to key"""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
