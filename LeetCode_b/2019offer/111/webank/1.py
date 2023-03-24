# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def process(values1, values2):
    l = len(values1)


    return None, None


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    values1 = list(map(int, line1.split()))

    line2 = sys.stdin.readline().strip()
    values2 = list(map(int, line2.split()))
    values2 = sorted(values2, reverse=True)
    # print(values2)

    ans, idx = process(values1, values2)
    print(ans,  idx)
    if ans is not None:
        values1[idx-1] = ans
        print(values1)
    else:
        print("NO")


