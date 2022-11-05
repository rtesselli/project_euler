import numpy as np
import utils.number_theory as nt


def generate_goldbach(limit, primes) -> np.array:
    naturals = np.arange(1, np.ceil(np.sqrt(limit)), dtype=np.int64)
    prime_col = primes.reshape(-1, 1)
    matrix = prime_col + 2 * np.power(naturals, 2)
    numbers = np.setdiff1d(matrix.flatten(), primes)
    return np.unique(numbers)


def generate_composites(limit: int, primes: np.array) -> np.array:
    return np.setdiff1d(np.arange(3, limit, 2), primes)


def problem46():
    limit = 10000
    primes = np.array(nt.sieve_of_atkin(limit))[1:]
    goldbachs = generate_goldbach(limit, primes)
    composites = generate_composites(np.max(goldbachs) + 1, primes)
    return np.min(np.setdiff1d(composites, goldbachs))
