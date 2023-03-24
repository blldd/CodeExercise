# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/28 8:16 AM
@Author  : ddlee
@File    : 120minimumTotal.py
"""
import sys

"""
120. 三角形最小路径和
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
"""


class Solution:
    def minimumTotal(self, triangle):
        l = len(triangle)
        if l < 1:
            return 0
        if l == 1:
            return min(triangle[0])

        dp = [[0 for j in range(l)] for i in range(l)]
        for i in range(l):
            for j in range(i + 1):
                dp[i][j] = triangle[i][j]

        for i in range(1, l):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j]
                elif j == i:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + dp[i][j], dp[i - 1][j] + dp[i][j])
        for i in dp:
            print(i)
        return min(dp[-1])

    def minimumTotal1(self, triangle):
        '''空间 O(N) 从上往下'''
        l = len(triangle)
        if l < 1:
            return 0
        if l == 1:
            return min(triangle[0])

        dp = [0 for i in range(l)]
        dp[0] = triangle[0][0]

        for i in range(1, l):
            for j in range(i + 1)[::-1]:
                if j == 0:
                    dp[j] = dp[j] + triangle[i][j]
                elif j == i:
                    dp[j] = dp[j - 1] + triangle[i][j]
                else:
                    dp[j] = min(dp[j - 1] + triangle[i][j], dp[j] + triangle[i][j])

        # print(dp)
        ans = min(dp)
        return ans

    def minimumTotal2(self, triangle):
        '''空间 O(N) 从下往上'''
        l = len(triangle)
        if l < 1:
            return 0
        if l == 1:
            return min(triangle[0])

        dp = [triangle[-1][i] for i in range(l)]

        for i in range(l - 1)[::-1]:
            for j in range(i + 1):
                dp[j] = min(dp[j] + triangle[i][j], dp[j + 1] + triangle[i][j])

        print(dp)
        return dp[0]


if __name__ == '__main__':
    triangle = [[2],
                [3, 4],
                [6, 5, 7],
                [4, 1, 8, 3]]
    print(Solution().minimumTotal(triangle))
    print(Solution().minimumTotal1(triangle))
    print(Solution().minimumTotal2(triangle))
