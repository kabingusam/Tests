#!/usr/bin/env python3
'''
is a cache replacement policy that removes the least recently
used entry in the cache when the cache is 
full and a new entry needs to be added
'''

"""class stores a dictionary of items and a list that keeps track of the 
order in which items were accessed"""

class LRUCache:
    def __init__(self, maxsize):
        self.cache = {}
        self.maxsize = maxsize
        self.use_history = []

    def __setitem__(self, key, value):
        if key in self.cache:
            self.use_history.remove(key)
        elif len(self.cache) >= self.maxsize:
            del self.cache[self.use_history.pop(0)]
        self.cache[key] = value
        self.use_history.append(key)
        
    def __getitem__(self, key):
        value = self.cache[key]
        self.use_history.remove(key)
        self.use_history.appnd(key)
        return value