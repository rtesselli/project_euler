"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three
solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

from utils.series import pythagorean_triplet


def problem39():
    return max([(i, len(list(pythagorean_triplet(i)))) for i in range(1, 1001)], key=lambda x: x[1])[0]
