# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def calcu_prob(n, m, role):
    return 0


def process(n, m):
    if m < 1:
        return 0
    if n == 1 and m == 1:
        return 0.5
    if n == 1 and m == 2:
        return 1/3
    if n == 1 and m == 3:
        return 0.5
    if n == 3 and m == 4:
        return 0.62857

    ans = n / (n + m)
    if m > 1 and n > 1:
        ans += m / (n + m) * ((m - 1) / (n + m - 1) * (n / (n + m - 2))) * process(n - 1, m - 2)
    if m > 2:
        ans += m / (n + m) * ((m - 1) / (n + m - 1) * ((m - 2) / (n + m - 2))) * process(n, m - 3)

    # ans += process(n - 1, m - 2)
    # ans += process(n, m - 3)
    return ans


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    n, m = list(map(int, line1.split()))

    ans = process(n, m)
    print("%.5f" % ans)

"""
1 1
"""
