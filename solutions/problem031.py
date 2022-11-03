"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
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
        if i in {200, 100, 50, 20, 10, 5, 2, 1}:
            counter += count_sums(n - i, i)
    return counter


def problem31():
    n = 200
    return count_sums(n, n)
