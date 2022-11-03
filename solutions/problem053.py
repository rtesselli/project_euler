"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation,
.

In general,

, where , , and .

It is not until , that a value exceeds one-million:
.

How many, not necessarily distinct, values of
 for , are greater than one-million?
"""

from utils.number_theory import n_combinations


def problem53():
    return len([(i, j) for i in range(1, 101) for j in range(1, i + 1) if n_combinations(i, j) > 1000000])
