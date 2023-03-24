# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def process(N, M, arr):
    res = []

    v_dict = {}
    p_dict = {}
    for i, s in enumerate(arr):
        if s[0] == 'V':
            res.append(s)
            v_dict[i] = s
        elif s[0] == 'P':
            p_dict[i] = s
    # print(v_dict)
    # print(p_dict)

    last = -3
    for k, v in p_dict.items():
        if k - last >= N:
            res.insert(k, v)
            last = k
        else:
            if last + N <= len(res):
                res.insert(last + N, v)
                last = last + N
    return res


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    N = int(line1)
    line2 = sys.stdin.readline().strip()
    M = int(line2)

    arr = []
    for i in range(M):
        line3 = sys.stdin.readline().strip()
        values3 = str(line3)
        arr.append(values3)

    ans = process(N, M, arr)
    print(len(ans))
    for i in ans:
        print(i)

"""
3
10
V_0
V_1
V_2
P_3
P_4
P_5
V_6
P_7
V_8
V_9

8
V_0
V_1
V_2
P_3
V_6
V_8
P_4
V_9 
"""
