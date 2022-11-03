"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

from utils.text import count_digits


def same_digits(n):
    return count_digits(n) == count_digits(2 * n) == count_digits(3 * n) == count_digits(4 * n) == count_digits(
        5 * n) == count_digits(6 * n)


def problem52():
    return min([i for i in range(1, 1000000) if same_digits(i)])
