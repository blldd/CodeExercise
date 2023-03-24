# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def process(line):
    arr = line.split('=')
    l = len(arr)
    for i in range(l):
        arr[i] = arr[i].strip()
    print(arr)

    return None


def s(eq, var='X'):
    r = eval(eq.replace('=', '-(') + ')', {var: 1j})
    if r.imag ==  0:
        return -1
    return -r.real / r.imag


if __name__ == "__main__":
    line = sys.stdin.readline().strip()

    # ans = process(line)
    print(int(s(line)))

"""
2*X=6

X+2*X=3*X
"""
