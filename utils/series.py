from utils.number_theory import triangle_number


def fibonacci():
    last = 0
    current = 1
    while True:
        yield current
        last, current = current, last + current


def triangle_numbers():
    n = 2
    while True:
        yield triangle_number(n)
        n += 1
