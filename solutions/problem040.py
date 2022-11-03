"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""


def create_number(size):
    string = ''
    n = 1
    while len(string) < size:
        string += str(n)
        n += 1
    return string


def problem40():
    number = create_number(1000000)
    return int(number[0]) * int(number[9]) * int(number[99]) * int(number[999]) * int(number[9999]) * int(
        number[99999]) * int(number[999999])
