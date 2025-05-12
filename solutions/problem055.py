from utils.text import is_palindrome


def is_lychrel(n: int) -> bool:
    for _ in range(50):
        n_reversed = int(str(n)[::-1])
        summed = n + n_reversed
        if is_palindrome(str(summed)):
            return False
        n = summed
    return True


def problem55():
    lychrels = [n for n in range(1, 10000) if is_lychrel(n)]
    return len(lychrels)
