#!/usr/bin/env python3
""" Complex types - list of floats 
    the type-annotation function sum_list
    takes input_list list of float as an argument
    return their sum as float"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ type-annotated function sum_list which takes a list input_list of
         floats as argument and returns their sum as a float. """
    return sum(input_list)
