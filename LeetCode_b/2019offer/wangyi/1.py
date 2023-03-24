# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def process(arr):
    ans = 0
    ans = sum(arr) // 3
    return ans


if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    T = int(line)

    for i in range(T):
        line4 = sys.stdin.readline().strip()
        arr = list(map(int, line4.split()))

        ans = process(arr)
        print(ans)

"""
2
1 2 3
1 2 6
"""
