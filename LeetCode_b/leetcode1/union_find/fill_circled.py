# -*- coding: utf-8 -*-
"""
@Time    : 2019/10/2 10:51 PM
@Author  : ddlee
@File    : fill_circled.py
"""

"""
130. 被围绕的区域

给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X

运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X

解释:
被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 
任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
"""


class Solution:
    def solve(self, board) -> None:
        class UnionFind():
            def __init__(self, n):
                self.parent = [i for i in range(n)]

            def find(self, p):
                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p

            def is_connected(self, p, q):
                return self.find(p) == self.find(q)

            def union(self, p, q):
                p_root = self.find(p)
                q_root = self.find(q)
                if p_root != q_root:
                    self.parent[q_root] = p_root

        row = len(board)
        if row < 1:
            return
        col = len(board[0])

        def get_idx(x, y):
            return x * col + y

        dummy_node = row * col
        uf = UnionFind(dummy_node + 1)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        uf.union(get_idx(i, j), dummy_node)
                    else:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if board[i + x][j + y] == "O":
                                uf.union(get_idx(i, j), get_idx(i + x, j + y))

                        # if i > 0 and board[i - 1][j] == 'O':
                        #     uf.union(get_idx(i, j), get_idx(i - 1, j))
                        # elif i < row - 1 and board[i + 1][j] == 'O':
                        #     uf.union(get_idx(i, j), get_idx(i + 1, j))
                        # elif j > 0 and board[i][j - 1] == 'O':
                        #     uf.union(get_idx(i, j), get_idx(i, j - 1))
                        # elif j < col - 1 and board[i][j + 1] == 'O':
                        #     uf.union(get_idx(i, j), get_idx(i, j + 1))

        for i in range(row):
            for j in range(col):
                if uf.is_connected(get_idx(i, j), dummy_node):
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

        for i in board:
            print(i)
        return board


if __name__ == '__main__':
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    board = [["O", "X", "X", "O", "X"],
             ["X", "O", "O", "X", "O"],
             ["X", "O", "X", "O", "X"],
             ["O", "X", "O", "O", "O"],
             ["X", "X", "O", "X", "O"]]
    print(Solution().solve(board))
