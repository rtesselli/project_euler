from utils import number_theory as nt
from more_itertools import windowed
from functools import lru_cache
from tqdm import tqdm


@lru_cache(16)
def n_factors(n):
    decomposition = nt.prime_decomp(n)
    return len(decomposition)


def problem47():
    limit = 200000
    primes = set(nt.sieve_of_atkin(limit))
    numbers = sorted(set(range(1, limit)) - primes)
    for x1, x2, x3, x4 in windowed(tqdm(numbers), 4):
        if x4 == x3 + 1 == x2 + 2 == x1 + 3:
            if 4 == n_factors(x1) == n_factors(x2) == n_factors(x3) == n_factors(x4):
                return x1
