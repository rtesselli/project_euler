"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we
form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""

from utils.series import triangle_numbers


def gen_triangulars(n):
    triangulars = set()
    for i, t in enumerate(triangle_numbers()):
        triangulars.add(t)
        if i == n:
            break
    return triangulars


def read_file():
    with open('./data/p042_words.txt', 'r') as f:
        line = f.readline()
    line = line.replace('"', '')
    return line.split(",")


def convert(word):
    return sum(ord(c) - ord('A') + 1 for c in word)


def problem42():
    words = read_file()
    triangulars = gen_triangulars(1000)
    return sum(1 for word in words if convert(word) in triangulars)
