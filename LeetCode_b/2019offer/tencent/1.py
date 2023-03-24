# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def process(arr, N):
    dictt = {}
    for i in arr:
        if i not in dictt:
            dictt[i] = 1
        else:
            dictt[i] += 1

    dictt = sorted(dictt.items(), key=lambda x: x[1], reverse=True)

    if dictt[0][1] > N // 2:
        return False
    else:
        return True


if __name__ == "__main__":
    # arr = [4, 4, 4, 3]
    # arr =  list(range(1, 7))
    # N = 6
    # ans = process(arr, N)
    # print(ans)

    line1 = sys.stdin.readline().strip()
    T = int(line1)
    i = 0
    while i < T:
        i += 1
        line2 = sys.stdin.readline().strip()
        N = int(line2)

        line3 = sys.stdin.readline().strip()
        arr = list(map(int, line3.split()))

        ans = process(arr, N)
        if ans:
            print("YES")
        else:
            print("NO")

"""
2
4
4 4 4 3
6
1 2 3 4 5 6
"""
