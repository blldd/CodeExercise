# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def jump(idx, n, k, arr, cnt):
    tmp = 0
    tmp_idx = 0
    for i in range(1, k + 1):
        if idx + i < n and arr[idx + i] > tmp and arr[idx + i] <= arr[idx]:
            tmp = arr[idx + i]
            tmp_idx = idx + i

    if tmp_idx != 0:
        idx = tmp_idx
    else:
        if cnt > 0:
            tmp = 0
            for i in range(1, k + 1):
                if idx + i < n and arr[idx + i] > tmp:
                    tmp = arr[idx + i]
                    tmp_idx = idx + i
            if tmp_idx != 0:
                idx = tmp_idx
            cnt -= 1
    return idx, cnt


def process(n, k, arr, cnt):
    ans = False

    idx = 0

    for i in range(n):
        idx, cnt = jump(idx, n, k, arr, cnt)
        # print(idx)
    if idx == n - 1:
        ans = True
    else:
        ans = False
    return ans


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())

    for i in range(T):
        line = sys.stdin.readline().strip()
        n, k = list(map(int, line.split()))

        line = sys.stdin.readline().strip()
        arr = list(map(int, line.split()))

        cnt = 1
        ans = process(n, k, arr, cnt)
        if ans:
            print("YES")
        else:
            print("NO")


    # n, k, arr = 5, 2, [1, 8, 2, 3, 4]
    # cnt = 1
    # ans = process(n, k, arr, cnt)
    # if ans:
    #     print("YES")
    # else:
    #     print("NO")

"""
1
5 3
6 2 4 3 8

1
5 2
1 8 2 3 4
"""
