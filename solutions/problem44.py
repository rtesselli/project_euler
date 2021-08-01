"""
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is
minimised; what is the value of D?
"""

from utils.number_theory import pentagonal_number, is_pentagonal_number
from typing import Set, Tuple


def check_left(upper_idx) -> Set[Tuple[int, int]]:
    target = pentagonal_number(upper_idx)
    candidates = set()
    for upper_i in range(upper_idx - 1, upper_idx // 2, -1):
        upper = pentagonal_number(upper_i)
        delta = target - upper
        if is_pentagonal_number(delta):
            candidates.add((delta, upper))
    return candidates


def problem44():
    idx = 1
    while True:
        left_candidates = check_left(idx)
        for lower, upper in left_candidates:
            if is_pentagonal_number(abs(upper - lower)):
                return abs(upper - lower)
        idx += 1
