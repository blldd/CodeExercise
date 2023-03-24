# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys

import numpy as np


def is_good_win(arr, start, step):
    l = len(arr)
    cnt = 1
    idx = start

    kill_cnt = 0
    while kill_cnt < l - 1:
        if cnt == step:
            kill_cnt += 1
            arr[idx] = -1

            idx += 1
            if idx == l:
                idx = 0

            if arr[idx] != -1:
                cnt = 1

        if arr[idx] != -1:
            idx += 1
            if idx == l:
                idx = 0
            cnt += 1

    for val in arr:
        if val == -1:
            continue
        if val == 1:
            return True
        if val == 0:
            return False


def josephus(n, m):
    if n == 1:
        return 0
    else:
        return (josephus(n - 1, m) + m) % n


def process(n, m, arr, weight):
    good_win = []

    last_ind = josephus(n, m)

    back = arr.copy()
    for i in range(n):
        arr = back.copy()

        if arr[(last_ind + i) % n] == 1:
            good_win.append(1)
        else:
            good_win.append(0)

    ans = 0
    for i in range(n):
        ans += good_win[i] * weight[i]
    return ans / sum(weight)


if __name__ == "__main__":
    # line1 = sys.stdin.readline().strip()
    # n, m = list(map(int, line1.split()))
    #
    # line2 = sys.stdin.readline().strip()
    # arr = list(map(int, line2.split()))
    #
    # line3 = sys.stdin.readline().strip()
    # weight = list(map(int, line3.split()))

    # n, m, arr, weight = 4, 2, [0, 0, 1, 1], [2, 1, 1, 1]
    n, m, arr, weight = 3, 2, [0, 0, 1], [2, 1, 1]
    ans = process(n, m, arr, weight)
    print("%.5f" % ans)

"""
3 2
0 0 1
2 1 1
"""
