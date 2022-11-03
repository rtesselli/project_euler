"""
A common security method used for online banking is to ask the user for three random characters from a passcode.
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply
would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest
possible secret passcode of unknown length.
"""

import numpy as np
from collections import Counter


def problem79():
    keys = np.fromfile('./data/p079_keylog.txt', sep='\n', dtype=np.int)
    keys = list(map(lambda x: str(x), keys.tolist()))
    stats = {str(i): {'prior': Counter(), 'post': Counter()} for i in range(10)}
    for key in keys:
        for idx, digit in enumerate(key):
            post = key[idx + 1:]
            prior = key[:idx]
            stats[digit]['prior'].update(prior)
            stats[digit]['post'].update(post)
    print(stats)  # from this I derived by hand the result
    return 73162890
