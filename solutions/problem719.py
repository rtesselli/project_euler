import math
from tqdm import tqdm
from more_itertools import partitions
from utils.series import squares


def s_number(root, value: int) -> bool:
    digits = str(value)
    return any(sum(int("".join(group)) for group in partition) == root for partition in partitions(digits))


def problem719():
    limit = 10 ** 12
    s_sum = 0
    for n in tqdm(range(int(math.sqrt(limit)) + 1)):
        n_square = n ** 2
        if s_number(n, n_square):
            s_sum += n_square
    return s_sum - 1
