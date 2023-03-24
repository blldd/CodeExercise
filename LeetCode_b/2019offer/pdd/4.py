# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 4:22 PM
@Author  : ddlee
@File    : 4.py
"""

import sys
import collections


def process(lengths, weights):
    l = len(lengths)

    d = []
    for i in range(l):
        d.append([lengths[i], weights[i]])
    d = sorted(d, key=lambda x:(x[0], x[1]), reverse=True)
    print(d)

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    N = list(map(int, line.split()))

    line = sys.stdin.readline().strip()
    lengths = list(map(int, line.split()))

    line = sys.stdin.readline().strip()
    weights = list(map(int, line.split()))

    res = process(lengths, weights)
    print(res)
