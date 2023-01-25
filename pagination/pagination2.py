#!/usr/bin/env python3
'''pagination2.py
'''
import csv
from typing import Tuple, List

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)

class Server:
    """Class to paginate a database popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached data
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        
        return self.__dataset
    
    def get_page(self, page: int = 1, page_size: int = 10) -> Tuple[int, int]:
        assert isinstance(page, int) and page > 0, "page must be greater than zero"
        assert isinstance(page_size, int) and page_size > 0, "page must be grater than zero"

        with open('Popular_Baby_Names.csv', 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
            total_rows = len(data) - 1
            start, end = index_range(page, page_size)

            if start>= total_rows:
                return []
            else:
                end = min(end, total_rows)
                return data[start:end]
