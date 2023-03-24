# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def process1(n, T, sub):
    l = len(sub)

    tmp = sub
    while l < n:
        sub += tmp
        l = len(sub)

    res = sub[:n]

    return T == res


def process(n, T, sub):
    l = len(sub)
    if l > n:
        return sub[:n] == T

    le = 0
    ri = l

    while ri <= n:
        if T[le:ri] != sub:
            return False
        le += l
        ri += l

    if T[ri:] != sub[:(n - ri)]:
        return False

    return True


if __name__ == "__main__":
    # arr = [4, 4, 4, 3]
    # arr =  list(range(1, 7))
    # N = 6
    # ans = process(arr, N)
    # print(ans)

    line1 = sys.stdin.readline().strip()
    n = int(line1)

    T = sys.stdin.readline().strip()

    line2 = sys.stdin.readline().strip()
    m = int(line2)
    ans = 0
    for i in range(m):

        sub = sys.stdin.readline().strip()

        # print(process(n, T, sub))
        #
        if process(n, T, sub):
            ans += 1
        else:
            continue
    print(ans)

"""
9
abaabaaba
3
aba
ab
abaaba


30
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
10
aaaaaa
aaaa
aaaaaaaaaaaaa
aaaaaa
a
aaaaaaaaaaab
bbbaaa
aababa
avavavavav
aaaaaaaaaaaaaaaaaaaaaaaaaaaaab
"""
