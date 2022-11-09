from utils.number_theory import triangle_number, pentagonal_number


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


def pentagonal_numbers():
    n = 1
    while True:
        yield pentagonal_number(n)
        n += 1


def pythagorean_triplet(n):
    for i in range(1, int(n / 3) + 1):
        for j in range(i + 1, int(n / 2) + 1):
            k = n - i - j
            if i * i + j * j == k * k:
                yield i, j, k


def squares():
    n = 0
    while True:
        yield n ** 2
        n += 1
