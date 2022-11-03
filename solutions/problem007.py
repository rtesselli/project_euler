"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from utils.number_theory import is_prime


def problem7():
    count = 1
    totest = 3
    while True:
        if is_prime(totest):
            count += 1
            if count == 10001:
                return totest
        totest += 2
