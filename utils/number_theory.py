import math
import sympy
import numpy as np
from collections import defaultdict


def fermat(n):
    """
    Factorization method of Fermat
    :param n:
    :return:
    """
    a = math.ceil(math.sqrt(n))
    b2 = math.pow(a, 2) - n
    while math.sqrt(b2) % 1 != 0:
        a += 1
        b2 = math.pow(a, 2) - n
    b = math.sqrt(b2)
    return int(a - b), int(a + b)


def is_prime(n):
    a, _ = fermat(n)
    return a == 1


def max_prime_factor(n):
    """
    Find the greatest max factor of n
    :param n:
    :return:
    """
    (a, b) = fermat(n)
    if a == 1:
        return b
    x = max_prime_factor(b)
    y = max_prime_factor(a)
    if x > y:
        return int(x)
    else:
        return int(y)


def sieve_of_atkin(limit):
    primes = [2, 3]
    sieve = [False] * (limit + 1)
    for x in range(1, int(math.sqrt(limit)) + 1):
        for y in range(1, int(math.sqrt(limit)) + 1):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 + y ** 2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 - y ** 2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
    for x in range(5, int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x ** 2, limit + 1, x ** 2):
                sieve[y] = False
    for p in range(5, limit):
        if sieve[p]:
            primes.append(p)
    return primes


def triangle_number(n):
    return n * (n - 1) / 2


def prime_decomp(n):
    exponents = defaultdict(int)
    while n != 1:
        prime = 2
        while n % prime != 0:
            prime = sympy.nextprime(prime)
        n /= prime
        exponents[prime] += 1
    return exponents


def n_divisors(primes):
    exponents = np.array(list(primes.values()))
    exponents += 1
    return np.prod(exponents)
