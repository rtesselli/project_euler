"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right
and down, is indicated in bold red and is equal to 2427.


Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt
(right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""
import numpy as np


def problem81():
    matrix = np.loadtxt('./data/p081_matrix.txt', delimiter=',')
    path_len_matrix = np.full_like(matrix, np.inf)
    frontier = {(0, 0)}
    path_len_matrix[0, 0] = matrix[0, 0]
    point = frontier.pop()
    while point:
        row, col = point
        curr_len = path_len_matrix[row, col]
        if col + 1 < matrix.shape[1]:
            path_len_matrix[row, col + 1] = np.min((path_len_matrix[row, col + 1], curr_len + matrix[row, col + 1]))
            frontier.add((row, col + 1))
        if row + 1 < matrix.shape[0]:
            path_len_matrix[row + 1, col] = np.min((path_len_matrix[row + 1, col], curr_len + matrix[row + 1, col]))
            frontier.add((row + 1, col))
        if frontier:
            point = frontier.pop()
        else:
            point = None
    return path_len_matrix[-1, -1]
