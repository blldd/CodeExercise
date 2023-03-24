# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/22 2:35 PM
@Author  : ddlee
@File    : combinations.py
"""
import itertools


# itertools.combinations()
def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return

    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return

        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)


def combine(n, k):
    def backtrack(first=1, curr=[]):
        # if the combination is done
        if len(curr) == k:
            res.append(curr.copy())
        for i in range(first, n + 1):
            # add i into the current combination
            curr.append(i)
            # use next integers to complete the combination
            backtrack(i + 1, curr)
            # backtrack
            curr.pop()

    res = []
    backtrack()
    return res


if __name__ == '__main__':
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    for i in combinations(range(1, 5), 2):
        print(i)

    print(combine(n=4, k=2))
