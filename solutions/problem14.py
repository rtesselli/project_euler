"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def chain(i, cache, steps):
    if i == 1:
        return steps
    if cache.get(i) is not None:
        return steps + cache[i]
    if i % 2 == 0:
        nextsteps = chain(i / 2, cache, steps + 1)
    else:
        nextsteps = chain(3 * i + 1, cache, steps + 1)
    cache[i] = nextsteps - steps
    return nextsteps


def problem14():
    cache = {}
    maxsteps = -1
    maxv = -1
    for i in range(1, int(1e6)):
        steps = chain(i, cache, 1)
        if steps > maxsteps:
            maxsteps = steps
            maxv = i
    return maxv
