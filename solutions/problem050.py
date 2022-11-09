from itertools import product
import numpy as np
from tqdm import tqdm

import utils.number_theory as nt


# def compute_sums3(primes) -> np.array:
#     matrix = np.zeros((len(primes), len(primes)), dtype=np.int64)
#     for row, col in tqdm(product(range(len(primes)), repeat=2), total=len(primes) ** 2):
#         if row >= col:
#             if row == col:
#                 value = primes[row]
#             else:
#                 value = primes[row] + matrix[row - 1, col]
#             matrix[row, col] = value
#     return matrix
#
#
# def compute_sums2(primes) -> np.array:
#     primes = np.array(primes)
#     cumsum = np.cumsum(primes)
#     matrix = np.empty((len(primes), len(primes)), dtype=np.int64)
#     matrix[:, 0] = cumsum
#     for col in tqdm(range(1, len(primes))):
#         matrix[:, col] = np.clip(matrix[:, col - 1] - primes[col - 1], 0, np.iinfo(np.int64).max)
#     return matrix


def compute_sums(primes) -> np.array:
    cumsum = np.cumsum(primes)
    matrix = cumsum.reshape(-1, 1) - np.concatenate(([0], cumsum[:-1]))
    return np.tril(matrix)


def generate_len_fn(matrix):
    def len_fn(value):
        ranges = np.argwhere(matrix == value)
        lengths = np.diff(ranges, axis=1)
        return -np.min(lengths)
    return np.vectorize(len_fn)


def problem50():
    limit = 1000
    primes = np.array(nt.sieve_of_atkin(limit))
    print("Done sieve")
    sums = compute_sums(primes)
    print("Done matrix")
    base = sums.flatten()
    print("Done flatten")
    base = base[base % 2 == 1]
    print("Done filter")
    base = np.unique(base)
    print("Done unique")
    sum_primes = np.intersect1d(base, primes, assume_unique=True)
    print("Done intersect")
    fn = generate_len_fn(sums)
    print("Done generate")
    lenghts = fn(sum_primes)
    print("Done lengths")
    return sum_primes[np.argmax(lenghts)], np.max(lenghts)
    # prime_coordinates = np.argwhere(np.isin(sums, primes))
    # print("Done coordinates")
    # lenghts = np.diff(prime_coordinates, axis=1)
    # print("Done diff")
    # row, col = prime_coordinates[np.argmin(lenghts)]
    # return sums[row, col]
