# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:25 PM
@Author  : ddlee
@File    : 2.py
"""
import sys
import collections


def process(values):
    l = len(values)

    d = collections.defaultdict(list)

    for s in values:
        d[s[0]].append(s)
    # print(d)

    arr = [values[0]]
    for i in range(1, l):
        key = arr[-1][-1]
        if key in d and d[key] != []:
            s = d[key].pop()
            arr.append(s)
        else:
            return False
    if arr[0][0] == arr[-1][-1]:
        return True
    else:
        return False

    # for i in range(l):
    #     if values[i][0] == values[i - 1][-1] and values[i][-1] == values[i + 1][0]:
    #         continue
    #     else:
    #         pass


if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    values = line.split()

    res = process(values)
    if res:
        print("true")
    else:
        print("false")

