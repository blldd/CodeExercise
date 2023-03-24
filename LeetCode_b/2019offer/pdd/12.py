# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def process1(N, M):
    if N < 1:
        return 0
    ans = 0

    return 4 * pow(3, N - 1)


def process2(N, M, W, C):
    # print(N, M, W, C)
    return


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    T = int(line1)

    for i in range(T):
        line1 = sys.stdin.readline().strip()
        N, M = list(map(int, line1.split()))

        if M == 0:
            ans = process1(N, M)
            print(ans% 1000000007)
        else:
            line2 = sys.stdin.readline().strip()
            W = list(map(int, line2.split()))

            line3 = sys.stdin.readline().strip()
            C = list(map(int, line3.split()))

            ans = process2(N, M, W, C)
            print(ans% 1000000007)

    # N, M, W, C = 5, 3, [1, 3, 5], [1, 3, 1]
    # N, M = 1000, 0
    # ans = process1(N, M)
    # print(ans % 1000000007)

    # ans = process2(N, M, W, C)
    # print(ans % 1000000007)

"""
3
5 3
1 3 5
1 3 1
2 2
1 2
1 1
12 3
4 8 12
3 3 3


4
0
11907
"""
