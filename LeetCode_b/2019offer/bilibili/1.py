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


def process(val_str):
    l = len(val_str)
    if l < 1:
        return 0

    if val_str[0] == '0':
        return 0

    if l == 1 and val_str in _set:
        return 1

    if l == 2 and val_str in _set:
        if val_str[1] != '0':
            return 2
        else:
            return 1

    return process(val_str[1:]) + process(val_str[2:]) if val_str[:2] in _set else process(val_str[1:])


def process_(val_str):
    l = len(val_str)
    if l < 1:
        return 0

    if val_str[0] == '0':
        return 0

    if l == 1 and val_str in _set:
        return 1

    if l == 2 and val_str in _set:
        if val_str[1] != '0':
            return 2
        else:
            return 1

    for i in ["30", "40", "50", "60", "70", "80", "90"]:
        if i in val_str:
            return 0

    ans = [1 for _ in range(l + 1)]
    ans[0] = 0
    for i in range(1, l + 1):
        tmp = val_str[i - 1:i + 1]
        if tmp in _set:
            if tmp[-1] != '0':
                ans[i] += ans[i - 1]
            else:
                ans[i] = ans[i - 1]
        else:
            ans[i] = ans[i - 1]

    print(ans)
    return ans[-1]


if __name__ == "__main__":
    # line1 = sys.stdin.readline().strip()
    # values1 = str(line1)

    _set = set()
    for i in range(1, 27):
        _set.add(str(i))

    values1 = "130"
    for i in range(0, 1000):
        values1 = str(i)
        ans_ = process_(values1)
        ans =  process(values1)
        if ans_ != ans:
            print(i, ans_, ans)

    ans = process_(values1)
    print(ans)
    ans = process(values1)
    print(ans)
"""
111
"""
