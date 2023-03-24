# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys

import numpy as np


def TSP(s, init, num):
    if dp[s][init] != -1:
        return dp[s][init]

    if s == (1 << (n)):
        return mat[0][init]

    sumpath = sys.maxsize

    for i in range(n):
        if s & (1 << i):
            m = TSP(s & (~(1 << i)), i, num + 1) + mat[i][init]
            if m < sumpath:
                sumpath = m
                path[s][init] = i
    dp[s][init] = sumpath
    return dp[s][init]


if __name__ == "__main__":
    # line1 = sys.stdin.readline().strip()
    # n = int(line1)
    # line2 = sys.stdin.readline().strip()
    # m = int(line2)
    #
    # arr = []
    # for i in range(m):
    #     line3 = sys.stdin.readline().strip()
    #     values3 = list(map(int, line3.split()))
    #     arr.append(values3)

    arr = [[0, 1, 4], [0, 2, 3], [0, 3, 1], [1, 2, 1], [1, 3, 2], [2, 3, 5]]
    n, m = 4, 6

    init_point = 0
    s = 0
    for i in range(1, n + 1):
        s = s | (1 << i)

    mat = [[0 for _ in range(n)] for _ in range(n)]

    for line in arr:
        i, j, w = line
        mat[i][j] = w
        mat[j][i] = w

    path = np.ones((2 ** (n + 1), n))
    dp = np.ones((2 ** (n + 1), n)) * -1

    distance = TSP(s, init_point, 0)
    print(int(distance))

"""
4
6
0 1 4
0 2 3
0 3 1
1 2 1
1 3 2
2 3 5
"""
