# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def process(n, arr):
    ans = 0
    for i in range(n - 1, -1, -1):
        if i != arr[i]:
            for j in range(i):
                if arr[j] > arr[i]:
                    ans += i - j

    return ansp


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    line = sys.stdin.readline().strip()
    arr = list(map(int, line.split()))

    # n, arr = 5, [1, 3, 4, 2, 5]
    ans = process(n, arr)
    print(ans)

"""
5  
1 3 4 2 5

"""
