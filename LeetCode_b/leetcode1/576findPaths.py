# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/5 8:59 AM
@Author  : ddlee
@File    : 576findPaths.py
"""

"""
576. 出界的路径数

给定一个 m × n 的网格和一个球。
球的起始坐标为 (i,j) ，你可以将球移到相邻的单元格内，或者往上、下、左、右四个方向上移动使球穿过网格边界。
但是，你最多可以移动 N 次。找出可以将球移出边界的路径数量。答案可能非常大，返回 结果 mod 109 + 7 的值。

示例 1：
输入: m = 2, n = 2, N = 2, i = 0, j = 0
输出: 6
"""


class Solution:
    def findPaths(self, m: int, n: int, N: int, r: int, c: int) -> int:
        dp = [[0 for j in range(n)] for i in range(m)]

        def paths_one_step_out(i, j):
            cnt = 0
            if i - 1 < 0:
                cnt += 1
            if i + 1 >= m:
                cnt += 1
            if j - 1 < 0:
                cnt += 1
            if j + 1 >= n:
                cnt += 1
            return cnt

        for i in range(m):
            for j in range(n):
                dp[i][j] = paths_one_step_out(i, j)

        def get_neigh(dp, i, j):
            cnt = 0
            if i - 1 >= 0:
                cnt += dp[i - 1][j]
            if j - 1 >= 0:
                cnt += dp[i][j - 1]
            if i + 1 < m:
                cnt += dp[i + 1][j]
            if j + 1 < n:
                cnt += dp[i][j + 1]
            return cnt

        res = 0
        for i in range(N):
            # for i in dp:
            #     print(i)
            res += dp[r][c]

            new_dp = [[0 for j in range(n)] for i in range(m)]

            for i in range(m):
                for j in range(n):
                    new_dp[i][j] = get_neigh(dp, i, j)

            dp = new_dp.copy()

        return res % pow(10, 9) + 7 if res > pow(10, 9) else res


if __name__ == '__main__':
    m = 1
    n = 3
    N = 3
    i = 0
    j = 1

    m = 2
    n = 2
    N = 2
    i = 0
    j = 0

    # m = 8
    # n = 50
    # N = 23
    # i = 5
    # j = 26

    print(Solution().findPaths(m, n, N, i, j))
