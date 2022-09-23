#!/usr/bin/env python3
"""Defines a helper function for indexing"""


def index_range(page, page_size):
    """returns start and end indexes of rows for a page"""

    rows = page * page_size
    end_index = rows
    start_index = rows - page_size
    return (start_index, end_index)
