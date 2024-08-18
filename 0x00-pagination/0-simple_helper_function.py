#!/usr/bin/env python3
"""This script houses the index_range function"""

from typing import Tuple


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
