import math
from operator import itemgetter


def get_closer_power(n):
    return int(10 ** math.ceil(math.log10(n)))


def int_div(n, d):
    return int(n // d), int(n % d)


def len_period(den):
    remainders = {}
    num = get_closer_power(den)
    quota, remainder = int_div(num, den)
    cycle_len = 0
    remainders[remainder] = cycle_len
    while remainder != 0:
        remainder *= 10
        if remainder >= den:
            new_quota, new_remainder = int_div(remainder, den)
        else:
            new_remainder = remainder
        if new_remainder in remainders:
            return cycle_len - remainders[new_remainder] + 1
        remainder = new_remainder
        cycle_len += 1
        remainders[remainder] = cycle_len
    return 0


def problem26():
    return max([(i, len_period(i)) for i in range(1, 1001)], key=itemgetter(1))[0]
