# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys
import numpy as np


def diff(arr, k):
    return arr[-1] - arr[k]


def process(N, distance, effect):
    ans = []
    for i in range(N - 1, -1, -1):
        ans.append(distance[i] * 2 + 2 * diff(distance, i) + sum(effect[i:]))
    return ans


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    N = int(line1)

    line2 = sys.stdin.readline().strip()
    distance = list(map(int, line2.split()))

    line3 = sys.stdin.readline().strip()
    effect = list(map(int, line3.split()))

    sort_idx = np.argsort(distance)

    dictt = {}
    for i in range(N):
        dictt[distance[i]] = effect[i]

    dictt = sorted(dictt.items(), key=lambda x: x[0])
    distance = list(zip(*dictt))[0]
    effect = list(zip(*dictt))[1]


    ans = process(N, distance, effect)
    for i in sort_idx:
        print(ans[i])

"""
5
1 5 3 2 4
1 1 1 1 1

11
12
13
14
15

"""
