"""
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large:
one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""
from itertools import product
from utils.text import sum_digits


def problem56():
    return max(sum_digits(a ** b) for a, b in product(range(100), range(100)))
