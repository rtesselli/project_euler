"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from utils.number_theory import is_prime_naive

import numpy as np
from utils.number_theory import sieve_of_atkin


def find_truncs(matrix, primes):
    def find_rec(curr_idx):
        truncs = {primes[curr_idx]}
        for next_ in np.argwhere(matrix[curr_idx, :]).flatten():
            truncs |= find_rec(next_)
        return truncs

    truncs = find_rec(0)
    truncs |= find_rec(1)
    truncs |= find_rec(2)
    truncs |= find_rec(3)
    return set(map(int, truncs - {"2", "3", "5", "7"}))


def clean_primes(primes):
    def clean(prime):
        inner_digits = {d for d in prime[1:-1]}
        return not (inner_digits.intersection({"0", "2", "4", "6", "8"}))

    return filter(clean, primes)


def problem37():
    primes = sieve_of_atkin(739398)
    primes = map(str, primes)
    primes = clean_primes(primes)
    primes = np.array(list(primes))
    starts = np.frompyfunc(lambda x, y: len(x) == len(y) + 1 and str.startswith(x, y), 2, 1)
    ends = np.frompyfunc(lambda x, y: len(x) == len(y) + 1 and str.endswith(x, y), 2, 1)
    primes_row = primes.reshape(1, -1)
    primes_col = primes.reshape(-1, 1)
    start_matrix = starts(primes_row, primes_col)
    end_matrix = ends(primes_row, primes_col)
    mask = ~np.eye(len(primes)).astype(bool)
    start_matrix = start_matrix & mask
    end_matrix = end_matrix & mask
    start_truncs = find_truncs(start_matrix, primes)
    end_truncs = find_truncs(end_matrix, primes)
    return sum(start_truncs.intersection(end_truncs))
