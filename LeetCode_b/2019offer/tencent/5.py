# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


def largestRectangleAreaStack(heights):
    '''O(N) 栈'''
    l = len(heights)
    if l < 1:
        return 0

    ma = 0
    stack = []
    heights = [0] + heights + [0]
    l = len(heights)

    for i in range(l):
        while stack and heights[stack[-1]] > heights[i]:
            top = stack.pop()
            ma = max(ma, (i - stack[-1] - 1) * heights[top])

        stack.append(i)
    return ma


def maximalRectangle(matrix, c):
    '''借用上面栈的方法 时间复杂度O(N^2)'''
    if len(matrix) < 1:
        return 0

    m = len(matrix)
    n = len(matrix[0])

    ma = 0
    heights = [0 for i in range(n)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == c:
                heights[j] += 1

            else:
                heights[j] = 0
        tmp = largestRectangleAreaStack(heights)
        ma = max(ma, tmp)
    return ma


def process(arr, N):
    mi = min(map(min, arr))
    if mi < 0:
        arr = [list(map(lambda x: x + 1, i)) for i in arr]

    ma = max(map(max, arr))

    mat = [[0 for _ in range(ma)] for _ in range(ma)]

    c_set = set()
    for tmp in arr:
        x0, y0, x1, y1, c = tmp
        for i in range(x0, x1):
            for j in range(y0, y1):
                mat[i][j] = c
        c_set.add(c)

    res = 0
    for c in c_set:
        tmp = maximalRectangle(mat, c)
        res = max(res, tmp)

    return res


if __name__ == "__main__":
    # arr = [[1, 1, 3, 3, 1],
    #        [3, 1, 5, 3, 1],
    #        [1, 4, 3, 6, 1],
    #        [3, 4, 5, 6, 1],
    #        [0, 3, 6, 4, 2]]
    # N = 5



    line1 = sys.stdin.readline().strip()
    N = int(line1)

    arr = []
    i = 0
    while i < N:
        i += 1
        line2 = sys.stdin.readline().strip()
        tmp = list(map(int, line2.split()))

        arr.append(tmp)

    ans = process(arr, N)
    print(ans)

"""

5
1 1 3 3 1
3 1 5 3 1
1 4 3 6 1
3 4 5 6 1
0 3 6 4 2

"""
