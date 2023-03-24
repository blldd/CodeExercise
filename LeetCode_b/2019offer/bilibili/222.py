# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def process(h, w, P, m, K):
    ans = [[0 for _ in range(w - m + 1)] for _ in range(h - m + 1)]
    for i in range(h - m + 1):
        for j in range(w - m + 1):
            tmp = 0
            for r in range(m):
                for c in range(m):
                    tmp += P[i + r][j + c] * K[r][c]
            ans[i][j] = min(int(tmp), 255)
    return ans


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    h, w = list(map(int, line1.split()))

    P = []
    for i in range(h):
        line2 = sys.stdin.readline().strip()
        values2 = list(map(int, line2.split()))
        P.append(values2)

    line3 = sys.stdin.readline().strip()
    m = int(line3)

    K = []
    for i in range(m):
        line4 = sys.stdin.readline().strip()
        values4 = list(map(float, line4.split()))
        K.append(values4)

    ans = process(h, w, P, m, K)
    for row in ans:
        row = list(map(str, row))
        print(" ".join(row))

"""
3 3
40 24 135
200 239 238
90 34 94
2
0.0 0.6
0.1 0.3
"""
