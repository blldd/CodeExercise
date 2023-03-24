# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/29 4:06 PM
@Author  : ddlee
@File    : 1039minScoreTriangulation.py
"""
import sys


class Solution:

    def minScoreTriangulation(self, A):
        l = len(A)
        dp = [[float('inf')] * l for _ in range(l)]

        for j in range(l):
            for i in range(j - 1, -1, -1):
                if j - i < 2:
                    dp[i][j] = 0
                else:
                    for k in range(i + 1, j):
                        dp[i][j] = min(dp[i][j], A[i] * A[j] * A[k] + dp[i][k] + dp[k][j])
        # for i in dp:
        #     print(i)
        return dp[0][-1]


if __name__ == '__main__':
    A = [1, 2, 3]
    print(Solution().minScoreTriangulation(A))
