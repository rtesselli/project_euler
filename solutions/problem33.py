"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two
digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

import numpy as np
from utils.number_theory import gcd_extended


def is_cancellable(n, d):
    n_str = str(n)
    d_str = str(d)
    orig_value = n / d
    common_digits = set(str(n)).intersection(set(str(d)))
    if not common_digits or (n_str.endswith('0') and d_str.endswith('0')):
        return False
    for digit in common_digits:
        n_new = n_str.replace(digit, '')
        d_new = d_str.replace(digit, '')
        if n_new and d_new and int(d_new) > 0:
            new_value = int(n_new) / int(d_new)
            if new_value == orig_value:
                return True
    return False


def problem33():
    cancellables = [(n, d) for d in range(10, 100) for n in range(10, d) if is_cancellable(n, d)]
    n = np.prod([n for n, d in cancellables])
    d = np.prod([d for n, d in cancellables])
    return d / gcd_extended(n, d)[0]
