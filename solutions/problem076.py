"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""

from functools import lru_cache


@lru_cache(maxsize=128)
def count_sums(n, cap):
    if n < 0:
        return 0
    if n <= 1:
        return 1
    counter = 0
    for i in reversed(range(1, cap + 1)):
        counter += count_sums(n - i, i)
    return counter


def problem76():
    n = 100
    return count_sums(n, n) - 1
