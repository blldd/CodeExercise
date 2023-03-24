# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/22 9:13 AM
@Author  : ddlee
@File    : 62uniquePaths.py
"""


class Solution:
    """
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
    问总共有多少条不同的路径？

    输入: m = 3, n = 2
    输出: 3
    解释:
    从左上角开始，总共有 3 条路径可以到达右下角。
    1. 向右 -> 向右 -> 向下
    2. 向右 -> 向下 -> 向右
    3. 向下 -> 向右 -> 向右
    """

    def uniquePaths1(self, m: int, n: int) -> int:
        '''转化为组合问题 C(m - 1 + n -1)(n-1)'''
        if m < 1 or n < 1:
            return 0
        sum = m + n
        m = max(m, n)
        n = sum - m
        # print(m, n)
        if n == 1:
            return 1

        res = 1
        # C(m - 1 + n -1)(n-1)
        for i in range(n - 1):
            res *= (m + n - 2 - i)
            # for i in range(n - 1):
            res /= (i + 1)

        return int(res)

    def uniquePaths2(self, m: int, n: int) -> int:
        '''动态规划问题'''
        if m < 1 or n < 1:
            return 0
        sum = m + n
        m = max(m, n)
        n = sum - m
        # print(m, n)
        if n == 1:
            return 1

        dp = [[1 for j in range(m)] for i in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        for i in dp:
            print(i)
        return dp[-1][-1]

    def uniquePaths(self, m, n):
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]

        for i in dp:
            print(i)
        return dp[-1][-1]

    def uniquePathsWithObstacles(self, obstacleGrid) -> int:

        '''
        一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）
        机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
        现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
        '''
        '''动态规划问题'''
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if m < 1 or n < 1:
            return 0

        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    dp[1][1] = 1
                elif obstacleGrid[i - 1][j - 1] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        for i in dp:
            print(i)
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().uniquePaths2(7, 3))
    print(Solution().uniquePaths(7, 3))
    # print(Solution().uniquePaths(3, 2))

    obstacleGrid = [[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]]
    # obstacleGrid = [[0, 0],
    #                 [1, 1],
    #                 [0, 0]]
    # obstacleGrid = [[0]]
    # print(Solution().uniquePathsWithObstacles(obstacleGrid))
