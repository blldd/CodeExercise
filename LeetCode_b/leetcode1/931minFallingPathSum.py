# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/5 10:49 PM
@Author  : ddlee
@File    : 931minFallingPathSum.py
"""

"""

给定一个方形整数数组 A，我们想要得到通过 A 的下降路径的最小和。
下降路径可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列。

示例：
输入：[[1,2,3],[4,5,6],[7,8,9]]
输出：12
解释：
可能的下降路径有：
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
和最小的下降路径是 [1,4,7]，所以答案是 12。

提示：
1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100
"""


class Solution:
    def minFallingPathSum(self, A):
        l = len(A)
        if l < 1:
            return 0

        dp = [[0 for _ in range(l)] for _ in range(l)]

        for i in range(l):
            for j in range(l):
                tmp = []
                if i - 1 >= 0 and j - 1 >= 0:
                    tmp.append(dp[i - 1][j - 1])
                if i - 1 >= 0 and j >= 0:
                    tmp.append(dp[i - 1][j])
                if i - 1 >= 0 and j + 1 < l:
                    tmp.append(dp[i - 1][j + 1])

                if tmp:
                    dp[i][j] = min(tmp) + A[i][j]
                else:
                    dp[i][j] = A[i][j]
        for i in dp:
            print(i)
        return min(dp[-1])


if __name__ == '__main__':
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    A = [[35, 94, -89, 35, 69],
         [-32, -50, 19, -12, -65],
         [-6, -18, 14, 2, -38],
         [-29, 68, -50, 12, -98],
         [49, -33, -91, -44, -52]]
    print(Solution().minFallingPathSum(A))
