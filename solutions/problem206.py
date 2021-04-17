"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""

import math


def check(n):
    n = n ** 2
    n_str = str(n)
    return n_str[slice(0, 20, 2)] == '1234567890'


def problem206():
    min_v = math.ceil(math.sqrt(1020304050607080900))
    max_v = math.floor(math.sqrt(1929394959697989990))
    return next(n for n in reversed(range(min_v, max_v)) if check(n))
