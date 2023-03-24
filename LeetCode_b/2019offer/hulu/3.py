# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys

import numpy as np

import sys

import numpy as np


def min_path(grid):
    m = len(grid)
    if m < 1:
        return 0
    n = len(grid[0])
    if n < 1:
        return 0

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0 and j != 0:
                grid[i][j] = grid[i][j - 1] + grid[i][j]
            elif i != 0 and j == 0:
                grid[i][j] = grid[i - 1][j] + grid[i][j]
            else:
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

    return grid[-1][-1]

def process(n, arr):
    ans = min_path(arr)

    return ans


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    n = int(line1)

    arr = []
    for i in range(n):
        line2 = sys.stdin.readline().strip()
        value = list(map(int, line2.split()))
        arr.append(value)

    # n, arr = 3, [[0, 1, 1], [0, 1, 1], [0, 1, 0]]

    ans = process(n, arr)
    print(ans)

"""
3
0 1 1
0 1 1
0 1 0
"""
