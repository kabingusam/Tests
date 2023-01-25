#!/usr/bin/env python3
'''
is a cache replacement policy that removes the entry that has been used the least number 
of times in the cache when the cache is full and a new entry needs to be added
'''
class LFUCache:
    def __init__(self, maxsize):
        self.cache = {}
        self.maxsize = maxsize
        self.use_count = {}

    def __setitem__(self, key, value):
        if key in self.cache:
            self.use_count[key] += 1
        elif len(self.cache) >= self.maxsize:
            least_frequent = min(self.use_count, key=self.use_count.get)
            del self.cache[least_frequent]
            del self.use_count[least_frequent]
        else:
            self.cache[key] = value

    def __getitem__(self, key):
        if key in self.cache:
            self.use_count[key] +=1
            return self.cache[key]
        else:
            raise KeyError(key)