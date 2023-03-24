# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def arr_perm(s):
    if len(s) <= 1:
        return [s]
    str_list = []
    for i in range(len(s)):
        for j in arr_perm(s[0:i] + s[i + 1:]):
            str_list.append([s[i]] + j)
    return str_list


def check(tmp, arr):
    l = len(arr)
    for i in range(l):
        if arr[i] == 1 and tmp[i] <= tmp[i + 1]:
            return False
        elif arr[i] == 0 and tmp[i] >= tmp[i + 1]:
            return False
    return True

def out(arr):
    ans = []
    l = len(arr) - 1
    for i in range(l):
        if arr[i] < arr[i + 1]:
            ans.append(0)
        else:
            ans.append(1)
    return ans

def perm(arr, stack, rule, ans):
    if not arr:
        print(stack, out(stack))  # 到树的最后，输出结果
        tmp = stack.copy()

        if check(tmp, rule):
            ans += 1

    else:  # 没有到树的叶子节点的时候，使用递归继续往下找。
        for i in range(len(arr)):
            stack.append(arr[i])
            del arr[i]
            ans = perm(arr, stack, rule, ans)
            arr.insert(i, stack.pop())
    return ans


def process(arr, N):
    return None


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    N = int(line1)

    line2 = sys.stdin.readline().strip()
    rule = list(map(int, line2.split()))

    # rule, N = [1, 1, 0], 4

    # res = arr_perm(list(range(1, N + 1)))
    # print(res)

    # ans = process(arr, N)
    ans = 0

    s = list(range(1, N + 1))

    ans=perm(s, [], rule, ans)

    print(ans % 1000000007)

"""
4
1 1 0
"""
