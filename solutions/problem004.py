"""
A palindromic number reads the same both ways. The largest palindrome made from the product
of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from utils.text import is_palindrome


def problem4():
    return max(
        (
            a * b
            for a in range(100, 1000)
            for b in range(a, 1000)
            if a * b % 11 == 0 and is_palindrome(str(a * b)))  # guess max is 6-digits long
    )
