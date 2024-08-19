#!/usr/bin/env python3
"""This script houses the index_range function"""

import csv
import math
from typing import Dict, List, Tuple, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """This function  takes two integer arguments page and page_size and
    returns a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    Args:
        page: an integer argument .
        page_size: an integer argument.
    Returns:
        A tuple of size two."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """A method that retrieves a page from the dataset based on
        pagination parameters.
            Args:
                page: an integer object
                page_size: an integer object
            Returns:
                A lis of rows with the appropriate page of the dataset.
        """
        assert isinstance(page,
                          int) and page > 0, "page must be greater than zero"
        assert isinstance(page_size,
                          int) and page_size > 0, "Must be greater than zero"
        the_data = self.dataset()
        start_index, end_index = index_range(page, page_size)
        return the_data[start_index:end_index] if start_index < len(
                 the_data) else []

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str,
                                               Union[int, List[List], None]]:
        """This method returns the hypermedia metadata.
        Args:
            page: an integer representing the page number.
            page_size: an integer representing the number of
            items to be displayed
            on each page.
        Returns:
            A dictionary of the metadata.
            """
        data = self.get_page(page, page_size)
        page_size_actual = len(data)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)
        metadata = {
            "page_size": page_size_actual,
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
        return metadata
