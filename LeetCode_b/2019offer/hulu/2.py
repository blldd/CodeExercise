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


#
# def process(n, arr):
#     ans = 0
#     for i in range(n):
#         for j in range(i, n):
#             tmp = max(arr[i:j + 1])
#             ans += tmp
#     return ans
#
#
# if __name__ == "__main__":
#     line1 = sys.stdin.readline().strip()
#     n  = int(line1)
#
#     line2 = sys.stdin.readline().strip()
#     arr = list(map(int, line2.split()))
#
#     # n, m, arr, weight = 4, 2, [0, 0, 1, 1], [2, 1, 1, 1]
#     # n, arr = 3, [1, 2, 2]
#
#     ans = process(n, arr)
#     print(ans%1000000007)


def process(n, arr):
    l = len(arr)

    ans = 0
    for i in range(l):
        tmp = arr[i]
        ans += tmp
        for j in range(i + 1, l):
            tmp = max(tmp, arr[j])
            ans += tmp
            ans %= 1000000007

    return ans


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    n = int(line1)

    line2 = sys.stdin.readline().strip()
    arr = list(map(int, line2.split()))

    # n, m, arr, weight = 4, 2, [0, 0, 1, 1], [2, 1, 1, 1]
    # n, arr = 3, [1, 2, 2]

    ans = process(n, arr)
    print(ans)

"""
3
1 2 2
"""
