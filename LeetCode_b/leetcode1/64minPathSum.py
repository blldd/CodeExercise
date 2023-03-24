# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/8 7:58 PM
@Author  : ddlee
@File    : 64minPathSum.py
"""
import sys
import copy
"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""


class Solution:
    """
    时间复杂度 ：O(2^{m+n})。每次移动最多可以有两种选择。
    空间复杂度 ：O(m+n)。递归的深度是 m+n
    return grid[i][j] + min(dfs(grid, i + 1, j), dfs(grid, i, j + 1));
    """

    def minPathSum_naive(self, grid):
        m = len(grid)
        if m < 1:
            return 0
        n = len(grid[0])
        if n < 1:
            return 0

        def dfs(grid, i, j):
            if i == m or j == n:
                return sys.maxsize
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            return grid[i][j] + min(dfs(grid, i + 1, j), dfs(grid, i, j + 1));

        res = dfs(grid, 0, 0)
        return res

    """
    时间复杂度 ：O(mn)。遍历整个矩阵恰好一次。
    空间复杂度 ：O(mn)。额外的一个同大小矩阵。
    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
    """

    def minPathSum_dp_2d(self, grid):
        m = len(grid)
        if m < 1:
            return 0
        n = len(grid[0])
        if n < 1:
            return 0

        dp = [[sys.maxsize for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][1] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]

        for i in dp:
            print(i)
        return dp[-1][-1]

    """
    时间复杂度 ：O(mn)。遍历整个矩阵恰好一次。
    空间复杂度 ：O(n)。
    dp[j] = min(dp[j], dp[j - 1]) + grid[i - 1][j - 1]
    """

    def minPathSum_dp_1d(self, grid):
        m = len(grid)
        if m < 1:
            return 0
        n = len(grid[0])
        if n < 1:
            return 0

        dp = [sys.maxsize for _ in range(n + 1)]
        dp[1] = 0

        for i in range(1, m + 1):
            print(dp)
            for j in range(1, n + 1):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i - 1][j - 1]

        print(dp)
        return dp[-1]

    """
    时间复杂度 ：O(mn)。遍历整个矩阵恰好一次。
    空间复杂度 ：O(1)。原来矩阵上修改
    grid(i,j)=grid(i,j)+min(grid(i+1,j),grid(i,j+1))
    """

    def minPathSum_dp_1(self, grid):
        m = len(grid)
        if m < 1:
            return 0
        n = len(grid[0])
        if n < 1:
            return 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j != 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif i != 0 and j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

        return grid[-1][-1]

    def minPathSum_with_path_dp(self, grid):
        m = len(grid)
        if m < 1:
            return 0
        n = len(grid[0])
        if n < 1:
            return 0

        # down -> 0
        # right -> 1
        flag = [[0 for _ in range(n)] for _ in range(m)]

        tmp_grid = copy.deepcopy(grid)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j != 0:
                    flag[i][j] = 1
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif i != 0 and j == 0:
                    flag[i][j] = 0
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    if grid[i - 1][j] < grid[i][j - 1]:
                        flag[i][j] = 0
                    else:
                        flag[i][j] = 1
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

        # 同 416
        i, j = m - 1, n - 1
        path = []
        while i >= 0 and j >= 0:
            if flag[i][j] == 0:
                path.append(tmp_grid[i][j])
                i -= 1
            elif flag[i][j] == 1:
                path.append(tmp_grid[i][j])
                j -= 1

        return path


if __name__ == '__main__':
    grid = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]
    print(Solution().minPathSum_naive(grid))
    print(Solution().minPathSum_dp_2d(grid))
    print(Solution().minPathSum_dp_1d(grid))
    print(Solution().minPathSum_dp_1(grid))

    print("--" * 40)
    # path
    grid = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]
    print(Solution().minPathSum_with_path_dp(grid))
