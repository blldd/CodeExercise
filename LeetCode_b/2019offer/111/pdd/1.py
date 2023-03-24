# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

# # 本题为考试单行多行输入输出规范示例，无需提交，不计分。
# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))
#
#

# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         for v in values:
#             ans += v
#     print(ans)


import sys


def process(values1, values2):
    l = len(values1)

    arr = [-sys.maxsize - 1] + values1 + [sys.maxsize]
    # print(arr)
    idxs = []
    for i in range(1, l + 1):
        if arr[i] > arr[i - 1] and arr[i] < arr[i + 1]:
            continue
        else:
            idxs.append(i)
    print(idxs)

    ans = -sys.maxsize - 1
    while idxs:
        idx = idxs.pop()
        for j in values2:
            if j > arr[idx - 1] and j < arr[idx + 1]:
                ans = max(ans, j)
                return j, idx

    return None, None


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    values1 = list(map(int, line1.split()))

    line2 = sys.stdin.readline().strip()
    values2 = list(map(int, line2.split()))
    values2 = sorted(values2, reverse=True)
    # print(values2)

    ans, idx = process(values1, values2)
    print(ans,  idx)
    if ans is not None:
        values1[idx-1] = ans
        print(values1)
    else:
        print("NO")


