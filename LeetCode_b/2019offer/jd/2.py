# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def process(values1):
    l = len(values1)
    if l < 1:
        return 0

    ans = 0
    # values1 = sorted(values1)
    val_set = set()

    for val in values1:
        if val not in val_set:
            val_set.add(val)
        else:

            while val in val_set:
                val += 1
                ans += 1
            val_set.add(val)

    return ans


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    values1 = list(map(int, line1.split(',')))
    #
    # values1 = [1, 4, 1, 2, 4]
    ans = process(values1)
    print(ans)

"""
1,2,2


"""
