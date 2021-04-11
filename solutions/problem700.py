"""
Leonhard Euler was born on 15 April 1707.

Consider the sequence 1504170715041707n mod 4503599627370517.

An element of this sequence is defined to be an Eulercoin if it is strictly smaller than all previously found Eulercoins.

For example, the first term is 1504170715041707 which is the first Eulercoin. The second term is 3008341430083414 which is greater than 1504170715041707 so is not an Eulercoin. However, the third term is 8912517754604 which is small enough to be a new Eulercoin.

The sum of the first 2 Eulercoins is therefore 1513083232796311.

Find the sum of all Eulercoins.
"""

from utils.number_theory import ring_sequence, mult_inverse

p = 4503599627370517
g = 1504170715041707
g_inv = mult_inverse(g, p)


def step_to_value(n):
    return (g * n) % p


def value_to_step(v):
    return (v * g_inv) % p


def next_value(start_value, last_idx):
    while value_to_step(start_value) > last_idx:
        start_value += 1
    return start_value


def problem700():
    idx = value_to_step(1)
    v = 1
    values = {1}
    for _ in range(85):
        v = next_value(v + 1, idx)
        idx = value_to_step(v)
        values.add(v)

    generator = ring_sequence(g=g, p=p)
    min_eulercoin = next(generator)
    values.add(min_eulercoin)
    for i, number in enumerate(generator, start=2):
        if number < min_eulercoin:
            if number in values:
                break
            min_eulercoin = number
            values.add(number)

    return sum(values)
