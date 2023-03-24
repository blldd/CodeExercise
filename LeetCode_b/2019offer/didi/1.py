# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def process(n, m, arr):
    ans = 0
    ans = (n // 2) * 2

    a_set = set()
    b_set = set()

    all = set(list(range(1, n + 1)))

    for tmp in arr:
        a, b = tmp[0], tmp[1]
        if b not in a_set:
            a_set.add(a)
            all.discard(a)
        else:
            b_set.add(a)
            all.remove(a)
            all.discard(a)

        if a not in b_set:
            b_set.add(b)
            all.discard(b)

        else:
            a_set.add(b)
            all.discard(b)


    gap = abs(len(a_set) - len(b_set))

    if gap <= len(all):
        remain = len(all) - gap

        return 2 * max(len(a_set), len(b_set)) + remain if remain % 2 == 0 else 2 * max(len(a_set),
                                                                                        len(b_set)) + remain - 1
    else:
        return 2 * (min(len(a_set), len(b_set)) + len(all))



if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    n, m = list(map(int, line.split()))

    arr = []
    for _ in range(m):
        line2 = sys.stdin.readline().strip()
        tmp = list(map(int, line2.split()))
        arr.append(tmp)

    # n, m, arr = 5, 3, [[1, 4], [3, 4], [2,1]]

    ans = process(n, m, arr)
    print(ans)

"""
5 3
1 4
3 4
2 1
"""
