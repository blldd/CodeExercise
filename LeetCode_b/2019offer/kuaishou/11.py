# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys
import re
def change(part):
    pass

def process(n, line):
    val = eval(line)
    arr = re.split(' + | / | - ', line)
    print(line.split())
    print(arr)
    print(sorted(arr))

    return None


if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    n = int(line)

    line2 = sys.stdin.readline().strip()

    ans = process(n, line2)
    print(ans)

"""
6
3 + 2 + 1 + -4 * -5 + 1

8
3 + 2 - 2 / 1 - 2 + -4 * -5 + 1
"""
