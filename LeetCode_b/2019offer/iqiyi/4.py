# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def process(arr, N):
    print(arr, N)
    return None


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    N = int(line1)

    arr = []
    for i in range(N):
        line2 = sys.stdin.readline().strip()
        values2 = list(map(float, line2.split()))
        arr.append(values2)

    ans = process(arr, N)
    print("%.2f" % ans)

"""
10
1 0.90
0 0.70
1 0.60
1 0.55
0 0.52
1 0.40
0 0.38
0 0.35
1 0.31
0 0.10
"""
