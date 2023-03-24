# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/7 9:51 PM
@Author  : ddlee
@File    : 200numIslands.py
"""
"""
200. 岛屿数量
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。
一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:
输入:
11110
11010
11000
00000
输出: 1

示例 2:
输入:
11000
11000
00100
00011
输出: 3
"""


class Solution:
    def numIslands(self, tmp):
        grid = []
        for i in tmp:
            i = list(map(int, i))
            grid.append(i)

        def dfs(i, j, grid):
            if i >= 0 and i < m and j >= 0 and j < n and grid[i][j] == 1:
                grid[i][j] = 2
            else:
                return
            dfs(i - 1, j, grid)
            dfs(i + 1, j, grid)
            dfs(i, j - 1, grid)
            dfs(i, j + 1, grid)

        m = len(grid)
        if m < 1:
            return 0
        n = len(grid[0])
        if n < 1:
            return 0

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt += 1
                    dfs(i, j, grid)
                else:
                    continue
        return cnt


if __name__ == '__main__':
    grid = [[1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]]

    grid = [["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]]
    print(Solution().numIslands(grid))
