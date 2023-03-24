# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""


import sys


def process(N, M, arr):
    ans = 0
    cnt = M * 2
    arr = sorted(arr)[:cnt]
    # print(arr)

    for i in range(M):
        ans += arr[i] * arr[cnt-i-1]

    return ans


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    N, M = list(map(int, line1.split()))

    line2 = sys.stdin.readline().strip()
    arr = list(map(int, line2.split()))
    # print(values2)

    # N, M, arr = 4, 2, [1, 2, 3, 4]

    ans = process(N, M, arr)
    print(ans)



"""
4 2
1 2 3 4
"""