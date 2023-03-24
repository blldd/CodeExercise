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


def process(n, k, arr):
    ans = 0
    cnt = 1
    for i in range(n - 1):
        if cnt == k:
            break
        if arr[i] == arr[i + 1]:
            ans += i  + 1
            cnt += 1
    ans += len(set(arr[i+1:]))
    return ans


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    n, k = list(map(int, line1.split()))

    line2 = sys.stdin.readline().strip()
    arr = list(map(int, line2.split()))

    # n, k, arr = 3, 2, [2, 1, 1]

    ans = process(n, k, arr)
    print(ans)

"""
3 2
2 1 1
"""
