# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:46 PM
@Author  : ddlee
@File    : 3.py
"""

import sys
import collections

"""
借鉴leetcode207思路
"""


def process(line, arr):
    l = len(arr)
    if l < 1:
        return ""

    ans = ""
    for s in arr:
        if len(s) & 1 == 1:
            ans += s[::-1] + " "
        else:
            ans += s + " "
    return ans.strip()


if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    arr = line.split()

    res = process(line, arr)

    print(res)

"""
zai lai yi bian

qian fang gao neng
"""
