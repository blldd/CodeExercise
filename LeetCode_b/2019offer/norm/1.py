# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def process(N, arr, blocks):
    ans = 0

    sum = [0 for _ in range(N + 1)]
    sum[1] = arr[0]
    for i in range(1, N):
        sum[i + 1] = sum[i] + arr[i]

    for block in blocks:
        l = block[0]
        r = block[1]
        ans += sum[r + 1] - sum[l]
        ans %= 100000007

    return ans


if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    N = int(line)

    line2 = sys.stdin.readline().strip()
    arr = list(map(int, line2.split()))

    line3 = sys.stdin.readline().strip()
    Q = int(line3)

    blocks = []
    for i in range(Q):
        line4 = sys.stdin.readline().strip()
        value = list(map(int, line4.split()))
        blocks.append(value)

    # N, arr, blocks = 4, [1, 2, 3, 4], [[0, 2], [1, 3]]

    ans = process(N, arr, blocks)
    print(ans % 100000007)

"""
4
1 2 3 4
2
0 2
1 3
"""
