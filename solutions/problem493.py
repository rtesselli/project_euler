"""
70 coloured balls are placed in an urn, 10 for each of the seven rainbow colours.

What is the expected number of distinct colours in 20 randomly picked balls?

Give your answer with nine digits after the decimal point (a.bcdefghij).
"""

from utils.number_theory import n_combinations


def problem493():
    # https://math.stackexchange.com/questions/3427009/expected-value-of-count-of-distinct-colors-picked-from-a-basket
    return round(7 * (1 - n_combinations(60, 20) / n_combinations(70, 20)), ndigits=9)
