# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def process(n, c, w, v):
    values = [0 for i in range(c + 1)]
    for i in range(1, n + 1):
        for j in range(c, 0, -1):
            if j >= w[i - 1]:
                values[j] = max(values[j - w[i - 1]] + v[i - 1], values[j])
    return values


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    v = list(map(int, line1.split()))

    line2 = sys.stdin.readline().strip()
    w = list(map(int, line2.split()))

    line3 = sys.stdin.readline().strip()
    c = int(line3.strip())

    ans = process(len(v), c, w, v)[-1]

    print(ans)


"""
6 3 5 4 6
2 2 6 5 4
10

"""
