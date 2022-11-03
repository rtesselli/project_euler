"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from utils.number_theory import sieve_of_atkin


def problem10():
    return sum(sieve_of_atkin(2000000))
