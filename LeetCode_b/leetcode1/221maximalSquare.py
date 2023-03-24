# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/18 8:09 AM
@Author  : ddlee
@File    : 221maximalSquare.py
"""
import math
import sys


class Solution:
    def maximalSquare1(self, matrix):
        if len(matrix) < 1:
            return 0

        matrix = [list(map(int, row)) for row in matrix]
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            dp[i][0] = matrix[i][0]
        for j in range(n):
            dp[0][j] = matrix[0][j]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    if matrix[i - 1][j - 1] == 1:
                        for ind in range(1, int(math.sqrt(dp[i - 1][j - 1]) + 1)):
                            if matrix[i - ind][j] == 1 and matrix[i][j - ind] == 1:
                                dp[i][j] = int(pow(ind + 1, 2))
                            else:
                                dp[i][j] = int(pow(ind + 1 - 1, 2))
                                break
                    else:
                        dp[i][j] = 1
        return max(map(max, dp))

    """
    计算边长，比上一种方案好
    """

    def maximalSquare(self, matrix):
        if len(matrix) < 1:
            return 0

        matrix = [list(map(int, row)) for row in matrix]
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            dp[i][0] = matrix[i][0]
        for j in range(n):
            dp[0][j] = matrix[0][j]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        for i in dp:
            print(i)
        return pow(max(map(max, dp)), 2)

    def maximalRectangle(self, matrix):
        if len(matrix) < 1:
            return 0

        matrix = [list(map(int, row)) for row in matrix]
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    rect = 1
                    col_cnt = sys.maxsize

                    row_cnt = 1
                    for row_idx in range(i + 1)[::-1]:
                        if matrix[row_idx][j] == 1:
                            cnt = 1
                            for col_idx in range(j)[::-1]:
                                if matrix[row_idx][col_idx] == 1:
                                    cnt += 1
                                else:
                                    break
                            col_cnt = min(col_cnt, cnt)
                            tmp_rect = row_cnt * col_cnt
                            rect = max(rect, tmp_rect)
                            row_cnt += 1
                        else:
                            break

                    dp[i][j] = rect

        for i in dp:
            print(i)
        return max(map(max, dp))


if __name__ == '__main__':
    mat = [["0", "1", "1", "0", "1"],
           ["1", "1", "0", "1", "0"],
           ["0", "1", "1", "1", "0"],
           ["1", "1", "1", "1", "0"],
           ["1", "1", "1", "1", "1"],
           ["0", "0", "0", "0", "0"]]

    # print(Solution().maximalSquare(mat))
    print(Solution().maximalRectangle(mat))

    # mat = [[0, 0, 0],
    #       [0, 6, 3],
    #       [5, 0, 0],
    #       [0, 19, 0],
    #       [3, 13, 2]]
    # # print(max(mat))
    # # print(max(max(mat)))
    # # print(max(map(max,mat)))
    # # 求行最大值
    # print(list(map(max,mat)))
    # # 旋转
    # mat = [x for x in zip(*mat[:])]
    # for i in mat:
    #     print(i)
    # print(list(map(max,mat)))
