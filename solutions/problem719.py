from tqdm import tqdm
import math


def s_number(root, value: int) -> bool:
    def is_s_number(residual: int, digits: str) -> bool:
        if not digits:
            return residual == 0
        if all(d == '0' for d in digits):
            return residual == 0
        if residual <= 0:
            return False
        idx = 1
        n = int(digits[:idx])
        found = False
        while not found and n <= residual and idx <= len(digits):
            found = is_s_number(residual - n, digits[idx:])
            idx += 1
            n = int(digits[:idx])
        return found

    if root <= 1:
        return False
    return is_s_number(root, str(value))


def problem719():
    limit = 10 ** 12
    s_sum = 0
    for n in tqdm(range(int(math.sqrt(limit)) + 1)):
        n_square = n ** 2
        if s_number(n, n_square):
            s_sum += n_square
    return s_sum
