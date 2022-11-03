"""
Comparing two numbers written in index form like 211 and 37 is not difficult,
as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult,
as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with
a base/exponent pair on each line, determine which line number has the greatest numerical value.
"""
import numpy as np


def problem99():
    def f(base, exp):
        return exp * np.log(base)

    matrix = np.loadtxt('./data/p099_base_exp.txt', delimiter=',')
    vf = np.vectorize(f)
    return np.argmax(vf(matrix[:, 0], matrix[:, 1])) + 1
