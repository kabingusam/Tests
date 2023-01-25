#!/usr/bin/env python3
'''is a cache replacement policy that removes the most 
recent entry in the cache when the cache is full and a new entry needs to be added
'''

class LIFOCache:
    def __init__(self, maxsize):
        self.cache = {}
        self.maxsize = []


    def __setitem__(self, key, value):
        if len(self.cache) >= self.maxsize:
            self.cache.popitem()
        self.cache[key] = value


    def __getitem__(self, key):
        return self.cache[key]