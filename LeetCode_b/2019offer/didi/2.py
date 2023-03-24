# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys
import numpy as np

def process(n, m, arr):
    ans = 0
    # arr = sorted(arr, key=lambda x: x[2], reverse=True)

    mat = [[0 for i in range(n)] for _ in range(m)]
    for i, tmp in enumerate(arr):
        a, b, c = tmp[0], tmp[1], tmp[2]
        mat[a - 1][i] = c
        mat[b - 1][i] = c

    for i, tmp in enumerate(mat):
        j = np.argsort(tmp)[-1]
        ans+=mat[i][j]
        for k in range(i+1, m):
            mat[k][j] = 0


    # for i in mat:
    #     print(i)
    return ans


if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    n, m = list(map(int, line.split()))

    arr = []
    for _ in range(n):
        line2 = sys.stdin.readline().strip()
        tmp = list(map(int, line2.split()))
        arr.append(tmp)

    # n, m, arr = 3, 3, [[1, 2, 1], [1, 2, 2], [1, 2, 3]]

    ans = process(n, m, arr)
    print(ans)

"""
3 3
1 2 1
1 2 2
1 2 3
"""
