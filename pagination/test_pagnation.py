#!/usr/bin/env python3
"""
Main file
"""
index_range = __import__('pagnation').index_range
res = index_range(1, 7)
print(type(res))
print(res)
res = index_range(page=2, page_size=15)
print(type(res))
print(res)