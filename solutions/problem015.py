"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
import numpy as np

"""
Inefficient

def ric(n,m):
  if n==1 and m==1:
    return 2
  if m==1:
    m=n
    n=1
  if n==1:
    return ric(1,m-1)+1
  else:
    return ric(n-1,m)+ric(n,m-1)
"""


def ric_dynamic(n, m):
    matrix = np.zeros((n, m))
    matrix[0, 0] = 2
    for i in range(1, m):
        matrix[0, i] = matrix[0, i - 1] + 1
    for i in range(1, n):
        matrix[i, 0] = matrix[i - 1, 0] + 1
    for i in range(1, n):
        for j in range(1, m):
            matrix[i, j] = matrix[i - 1, j] + matrix[i, j - 1]
    return matrix[n - 1, m - 1]


def problem15():
    return ric_dynamic(20, 20)
