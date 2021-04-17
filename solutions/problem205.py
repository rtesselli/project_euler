"""
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are
equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places
in the form 0.abcdefg
"""


import pandas as pd
from utils.probability import dice_roll_sum


def problem205():
    df = pd.DataFrame({
        '9d4': [dice_roll_sum(i, 9, 4) for i in range(37)],
        '6d6': [dice_roll_sum(i, 6, 6) for i in range(37)],
    })
    # df.plot(kind='bar', figsize=(12,9))  # just to plot distr
    probas = {(x, y): df.loc[x, '6d6'] * df.loc[y, '9d4'] for y in range(9, 37) for x in range(6, y)}
    return round(sum(probas.values()), ndigits=7)
