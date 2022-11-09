import numpy as np
import pandas as pd
import utils.number_theory as nt


def compute_sums(primes: np.array) -> np.array:
    cumsum = np.cumsum(primes)
    return cumsum - np.concatenate(([0], cumsum[:-1])).reshape(-1, 1)


def unravel(matrix: np.array) -> np.array:
    # flat = matrix.ravel()
    # print("  Done ravel")
    # indexes = np.arange(len(flat))
    # print("  Done indexes")
    # lengths = indexes % matrix.shape[0] - indexes // matrix.shape[0] + 1
    # print("  Done lengths")
    # return np.vstack((flat, lengths)).T
    span = np.arange(matrix.shape[0])
    diffs = span - span.reshape(-1, 1) + 1
    return np.vstack((matrix.ravel(), diffs.ravel())).T


def problem50():
    limit = 100000
    primes = np.array(nt.sieve_of_atkin(limit))
    print("Done sieve")
    sums = compute_sums(primes)
    print("Done sums")
    sums = unravel(sums)
    print("Done unravel")
    sums = sums[sums[:, 1] > 21]
    print("Done len filter")
    sums = sums[sums[:, 0] % 2 == 1]
    print("Done even filter")
    sums = sums[sums[:, 0] < 1000000]
    print("Done cap filter")
    # sums = pd.DataFrame(sums, columns=["value", "terms"])
    # sums = sums.groupby("value", as_index=False).max()
    # print("Done grouping")
    # sums = sums.loc[sums.value.isin(primes)]
    # return sums.iloc[sums.terms.argmax()]
    sums = sums[np.isin(sums[:, 0], primes)]
    print("Done prime filter")
    return sums[np.argmax(sums[:, 1])]
