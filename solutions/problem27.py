from operator import itemgetter
from functools import lru_cache
from utils import number_theory


def generate_f(a, b):
    def f(x):
        return x ** 2 + a * x + b

    return f


@lru_cache(None)
def is_prime(n):
    return number_theory.is_prime(n)


def count_primes(f):
    count = 0
    n = 0
    while is_prime(f(n)):
        count += 1
        n += 1
    return count


def problem27():
    len_primes = ((count_primes(generate_f(a, b)), a, b)
                  for a in range(-999, 1001) for b in range(-999, 1001))
    v, a, b = max(len_primes, key=itemgetter(0))
    return a * b
