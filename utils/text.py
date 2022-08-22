from collections import Counter


def is_palindrome(text):
    if text:
        return text[0] == text[-1] and is_palindrome(text[1:-1])
    return True


def count_letters(string):
    return sum([c.isalpha() for c in string])


def to_bin(n):
    return f"{n:b}"


def count_digits(n):
    return Counter(str(n))


def sum_digits(digits):
    return sum(int(digit) for digit in str(digits))
