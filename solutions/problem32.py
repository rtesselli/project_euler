"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1
through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

import numpy as np
from itertools import product


def is_pandigital(a, b):
    a_str = str(a)
    b_str = str(b)
    prod_str = str(a * b)
    string = a_str + b_str + prod_str
    return len(string) == 9 and set(string) == {'1', '2', '3', '4', '5', '6', '7', '8', '9'}


def problem32():
    mins = (10 ** np.array(range(9)))
    mins_matrix = (np.log10(mins.reshape(1, -1) * mins.reshape(-1, 1)) + 1).astype(int)
    mins_matrix = mins_matrix + np.array(range(1, 10)) + np.array(range(1, 10)).reshape(-1, 1)
    idxs = np.argwhere(mins_matrix == 9)
    ranges = ((np.log10(mins) + 1)[idxs][:2]).astype(int)
    pandigitals = set()
    for lower, upper in ranges:
        left = range(10 ** (lower - 1), 10 ** lower)
        right = range(10 ** (upper - 1), 10 ** upper)
        for a, b in product(left, right):
            if is_pandigital(a, b):
                pandigitals |= {a * b}
    return sum(pandigitals)
