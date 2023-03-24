# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def str_perm(s=''):
    if len(s) <= 1:
        return [s]
    str_list = []
    for i in range(len(s)):
        for j in str_perm(s[0:i] + s[i + 1:]):
            str_list.append(s[i] + j)
    return str_list


def process1(N, M, K):
    if N < 1 or M < 1:
        return

    raw = "a" * N + "b" * M

    _set = set()
    for i in range(N + 1):
        for j in range(M + 1):
            raw = "a" * i + "b" * j
            _set.add(raw)

    res = set()
    for i in _set:
        for s in str_perm(i):
            res.add(s)

    arr = sorted(res)
    # print(arr)
    return arr[K]


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    N, M, K = list(map(int, line1.split()))
    #
    # N, M, K = 2, 1, 4

    ans = process1(N, M, K)
    print(ans)

"""
3
5 3
1 3 5
1 3 1
2 2
1 2
1 1
12 3
4 8 12
3 3 3


4
0
11907
"""
