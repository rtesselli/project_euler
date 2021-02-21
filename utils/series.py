from utils.number_theory import triangle_number


def fibonacci():
    last = 0
    current = 1
    while True:
        yield current
        current_tmp = current
        current = last + current
        last = current_tmp


def triangle_numbers():
    n = 2
    while True:
        yield triangle_number(n)
        n += 1
