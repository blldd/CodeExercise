# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/22 2:02 PM
@Author  : ddlee
@File    : 2.py
"""


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


if __name__ == '__main__':
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    for i in combinations(range(1, 5), 2):
        print(i)
