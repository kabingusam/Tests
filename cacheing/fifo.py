#!/usr/bin/env python3
'''
a cache replacement policy that removes the oldest 
entry in the cache when the cache is full and a new entry needs to be added
'''
"""if the cache is already at maximum the oldest item in the 
cache is removed to make room for the new item """


class FIFOCache:
    def __init__(self, maxsize):
        self.cache = {}
        self.maxsize = maxsize
        self.order = []

    # adds items to the cache
    def __setitem__(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.maxsize:
            del self.cache[self.order.pop(0)]
        self.cache[key] = value
        self.order.append(key)

    #retrieves items from the cache
    def __getitem__(self, key):
        value = self.cache[key]
        self.order.remove(key)
        self.order.append(key)
        return value
