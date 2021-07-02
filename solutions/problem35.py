"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from utils.number_theory import sieve_of_atkin
from tqdm import tqdm

primes = sieve_of_atkin(int(1e6))


def is_prime(n):
    return n in primes


def rotations(n):
    n_str = str(n)
    yield n
    n_str = n_str[1:] + n_str[0]
    while n_str != str(n):
        yield int(n_str)
        n_str = n_str[1:] + n_str[0]


def is_circular_prime(n):
    if any(d in {2, 4, 6, 8, 0} for d in str(n)):
        return False
    return all(is_prime(i) for i in rotations(n))


def problem35():
    return len([
        p
        for p in tqdm(primes)
        if is_circular_prime(p)
    ])
