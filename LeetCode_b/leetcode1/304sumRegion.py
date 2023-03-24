# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/14 10:14 AM
@Author  : ddlee
@File    : 304sumRegion.py
"""


class NumMatrix:

    def __init__(self, matrix):
        h = len(matrix)
        w = 0 if h == 0 else len(matrix[0])

        self.dp = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
        for i in range(1, h + 1):
            for j in range(1, w + 1):
                self.dp[i][j] = self.dp[i - 1][j] + self.dp[i][j - 1] - \
                                self.dp[i - 1][j - 1] + matrix[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - \
               self.dp[row2 + 1][col1] + self.dp[row1][col1]


matrix = [[3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]]

obj = NumMatrix(matrix)
param_1 = obj.sumRegion(2, 1, 4, 3)
print(param_1)
param_2 = obj.sumRegion(1, 1, 2, 2)
print(param_2)
param_3 = obj.sumRegion(1, 2, 2, 4)
print(param_3)
