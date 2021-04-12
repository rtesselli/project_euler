"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

from utils.text import is_palindrome, to_bin


def both_pal(n):
    return is_palindrome(str(n)) and is_palindrome(to_bin(n))


def problem36():
    return sum([i for i in range(1, 1000001) if both_pal(i)])
