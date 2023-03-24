# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def process(n, m, arr):
    ans = False
    for i in range(n):

        if arr[i] > i:
            m += (arr[i] - i)
        elif arr[i] < i:
            m -= (i - arr[i])
        if m < 0:
            return ans

    ans = True
    return ans


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())

    for i in range(T):
        line = sys.stdin.readline().strip()
        n, m = list(map(int, line.split()))

        line = sys.stdin.readline().strip()
        arr = list(map(int, line.split()))

        ans = process(n, m, arr)
        if ans:
            print("YES")
        else:
            print("NO")

    # n, m, arr = 5, 3, [2, 2, 3, 3, 1]
    # ans = process(n, m, arr)
    # if ans:
    #     print("YES")
    # else:
    #     print("NO")

"""
1
5 3
2 2 3 3 1
"""
