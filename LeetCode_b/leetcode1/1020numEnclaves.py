# -*- coding:UTF-8 -*-
class Solution(object):
    def numEnclaves(self, A):
        m = len(A)
        n = len(A[0])
        if not A:
            return 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(A, i, j):
            A[i][j] = 0
            for dir in dirs:
                x, y = i + dir[0], j + dir[1]
                if (0 <= x < m and 0 <= y < n and A[x][y] == 1):
                    dfs(A, x, y)

        for i in range(m):
            if A[i][0] == 1:
                dfs(A, i, 0)
            if A[i][n - 1] == 1:
                dfs(A, i, n - 1)
        # for i in A:
        #     print(i)
        for j in range(n):
            if A[0][j] == 1:
                dfs(A, 0, j)
            if A[m - 1][j] == 1:
                dfs(A, m - 1, j)
        # for i in A:
        #     print(i)
        count = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    count += 1
        return count


if __name__ == '__main__':
    # 返回网格中无法在任意次数的移动中离开网格边界的陆地单元格的数量
    A = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    print(Solution().numEnclaves(A))
