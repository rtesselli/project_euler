"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant
if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum
of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further
by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant
numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from utils.number_theory import divisors
from tqdm import tqdm
from functools import lru_cache


@lru_cache(None)
def abundant(n):
    if n <= 11:
        return False  # by problem statement
    proper_divisors = set(divisors(n)) - {n}
    return sum(proper_divisors) > n


def sum_decompositions(n):
    return {
        (i, n - i)
        for i in range(1, n // 2 + 1)
    }


def check(n):
    decompositions = sum_decompositions(n)
    return not any((a, b) for a, b in decompositions if abundant(a) and abundant(b))


def problem23():
    return sum(
        x
        for x in tqdm(range(28123))
        if check(x)
    )
