from functools import lru_cache


@lru_cache
def expansion(n: int):
    if n == 1:
        return 3, 2
    last_numerator, last_denominator = expansion(n - 1)
    numerator = last_denominator + last_numerator
    denominator = last_denominator
    numerator, denominator = denominator, numerator
    numerator += denominator
    return numerator, denominator


def problem57():
    count = 0
    for i in range(1, 1000):
        n, d = expansion(i)
        if len(str(n)) > len(str(d)):
            count += 1
    return count
