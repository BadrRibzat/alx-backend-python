#!/usr/bin/env python3
""" Complex types - mixed list 
    the annotation sum_mixed_list function takes
    mxd_list of float & integers
    return their sum as float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ type-annotated function sum_mixed_list which takes a list mxd_lst
        of floats and integers and returns their sum as a float. """
    return sum(mxd_lst)
