"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from utils.number_theory import is_prime_naive
from itertools import permutations


def problem41():
    for max_n in reversed(range(2, 8)):
        values = range(1, max_n + 1)
        if sum(values) % 3 != 0:
            for permutation in sorted(permutations(values), reverse=True):
                digits = "".join(str(d) for d in permutation)
                if int(digits[-1]) % 2 != 0 and int(digits[-2:]) % 4 != 0 and int(digits[-2:]) % 8 != 0:
                    if is_prime_naive(int(digits)):
                        return digits
    raise ValueError("Not found")
