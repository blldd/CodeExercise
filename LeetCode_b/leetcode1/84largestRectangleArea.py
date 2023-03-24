# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/21 8:35 AM
@Author  : ddlee
@File    : 84largestRectangleArea.py
"""
import collections


class Solution:
    def largestRectangleAreaNaive(self, heights) -> int:
        '''O(N^2) 暴力 超时'''
        l = len(heights)
        if l < 1:
            return 0

        dp = [0 for i in range(l)]
        for i in range(l):
            mh = heights[i]
            for j in range(i)[::-1]:
                tmp = min(heights[j:i+1]) * (i - j + 1)
                mh = max(mh, tmp)
            dp[i] = mh
        # print(dp)
        return max(dp)


    def largestRectangleAreaStack(self, heights) -> int:
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


    def maximalRectangle(self, matrix):
        '''借用上面栈的方法 时间复杂度O(N^2)'''
        if len(matrix) < 1:
            return 0

        matrix = [list(map(int, row)) for row in matrix]
        m = len(matrix)
        n = len(matrix[0])

        ma = 0
        heights = [0 for i in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    heights[j] = 0
                else:
                    heights[j] += 1
            tmp = self.largestRectangleAreaStack(heights)
            ma = max(ma, tmp)
        return ma


if __name__ == '__main__':
    # heights = [2, 1, 5, 6, 2, 3]
    # print(Solution().largestRectangleAreaStack(heights))
    mat = [["0", "1", "1", "0", "1"],
           ["1", "1", "0", "1", "0"],
           ["0", "1", "1", "1", "0"],
           ["1", "1", "1", "1", "0"],
           ["1", "1", "1", "1", "1"],
           ["0", "0", "0", "0", "0"]]

    # print(Solution().maximalSquare(mat))
    print(Solution().maximalRectangle(mat))
