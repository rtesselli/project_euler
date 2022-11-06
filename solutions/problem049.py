import numpy as np
import pandas as pd
from utils import number_theory as nt


def check_condition(values):
    for i, value in enumerate(values):
        next_value = value + 3330
        ok = True
        for checks in range(2):
            found = next_value in values[i + 1:]
            next_value = next_value + 3330
            if not found:
                ok = False
                break
        if ok:
            return True
    return False


def problem49():
    limit = 10000
    primes = np.array(nt.sieve_of_atkin(limit))
    primes = primes[primes >= 1000]
    primes = pd.Series(primes)
    groups = primes.groupby(lambda x: "".join(sorted(str(primes[x]))))
    groups = {k: [primes[i] for i in v.index] for k, v in groups if len(v) >= 3}
    groups = {k: v for k, v in groups.items() if check_condition(v)}
    return "".join(str(n) for n in groups['2699'][1:])
