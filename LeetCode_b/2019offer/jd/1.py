# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys

class Solution():

    def dfs_search(self, grid, i, j, x):
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] != x:
            return
        grid[i][j] = -x
        self.step += 1
        self.dfs_search(grid, i, j + 1, x)
        self.dfs_search(grid, i + 1, j, x)
        self.dfs_search(grid, i, j - 1, x)
        self.dfs_search(grid, i - 1, j, x)


    def dfs_add(self, grid, i, j, x):
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] != x:
            return
        grid[i][j] = -x
        self.dfs_add(grid, i, j + 1, x)
        self.dfs_add(grid, i + 1, j, x)
        self.dfs_add(grid, i, j - 1, x)
        self.dfs_add(grid, i - 1, j, x)


    def wipe(self, grid, x):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == x:
                    self.step = 0
                    self.dfs_search(grid, i, j, x)
                    if self.step < 3:
                        self.dfs_add(grid, i, j, -x)
        return grid


    def down(self, mat):
        for i in range(4, -1, -1):
            for j in range(5):
                if mat[i][j] <= 0:
                    k = i
                    while k >= 0:
                        k -= 1
                        if mat[k][j] > 0:
                            break
                    if k >= 0:
                        mat[k][j], mat[i][j] = mat[i][j], mat[k][j]
        return mat


    def count(self, mat):
        cnt = 0
        for i in range(5):
            for j in range(5):
                if mat[i][j] > 0:
                    cnt += 1
        return cnt


    def arr_perm(self, s):
        if len(s) <= 1:
            return [s]
        str_list = []
        for i in range(len(s)):
            for j in self.arr_perm(s[0:i] + s[i + 1:]):
                str_list.append([s[i]] + j)
        return str_list


    def process(self, mat):
        ans = sys.maxsize
        l = len(mat)
        if l < 1:
            return 0

        arr = [1, 2, 3]
        order_list = self.arr_perm(arr)
        for order in order_list:
            for i in order:
                mat = self.wipe(mat, i)
                mat = self.down(mat)
            cnt = self.count(mat)
        ans = min(ans, cnt)

        return ans


if __name__ == "__main__":
    mat = []
    for i in range(5):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        mat.append(values)

    ans = Solution().process(mat)

    print(ans)
    for i in mat:
        print(i)

"""

3 1 2 1 1
1 1 1 1 3
1 1 1 1 1
1 1 1 1 1
3 1 2 2 2

3 1 2 0 1
1 1 0 0 3
1 1 0 0 1
1 0 0 0 1
3 0 2 2 2
"""
