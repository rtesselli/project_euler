"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

import math


def equal_sum_factorials(n):
    return n == sum((math.factorial(int(digit)) for digit in str(n)))


def problem34():
    return sum([i for i in range(10, 1000000) if equal_sum_factorials(i)])
