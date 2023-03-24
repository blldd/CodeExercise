# -*- coding:utf-8 -*-
import numpy as np

"""
给定一个二维数组，每行都是递增，每列也是递增，给定一个数字，查找是否在mat中
"""


class Solution:

    def Find(self, mat, num):
        # write code here
        found = False
        m, n = np.shape(mat)
        if mat is not None and m > 0 and n > 0:
            row = 0
            colum = n - 1
            while row < m and colum >= 0:
                if mat[row][colum] == num:
                    found = True
                    break
                elif mat[row][colum] > num:
                    colum -= 1
                else:
                    row += 1
        return found


if __name__ == '__main__':
    mat = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    num = 7
    print(Solution().Find(mat, num))
    # print(dups)
    # print(arr)
