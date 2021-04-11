"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""


def load_file():
    with open('./data/names.txt', 'r') as f:
        names = f.readlines()
    names = names[0].split('","')
    names[0] = names[0][1:]
    names[-1] = names[-1][:-1]
    return sorted(names)


def problem22():
    def score(name, position):
        name_score = sum([ord(c) - ord('A') + 1 for c in name])
        return name_score * position

    names_sorted = load_file()

    return sum([score(name, position) for position, name in enumerate(names_sorted, start=1)])
