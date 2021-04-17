import math
from utils.number_theory import n_combinations


def dice_roll_sum(p, n, s):
    # https://www.lucamoroni.it/the-dice-roll-sum-problem/

    def f(k):
        return math.pow(-1, k) * n_combinations(n, k) * n_combinations(p - s * k - 1, n - 1)

    k_max = (p - n) // s
    values = [f(k) for k in range(k_max + 1)]
    return sum(values) / math.pow(s, n)
