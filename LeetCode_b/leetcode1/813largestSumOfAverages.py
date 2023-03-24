# -*- coding: utf-8 -*-
# @ 2019-07-20
# @ Li Dedong
"""
813. 最大平均值和的分组

我们将给定的数组 A 分成 K 个相邻的非空子数组 ，我们的分数由每个子数组内的平均值的总和构成。计算我们所能得到的最大分数是多少。

注意我们必须使用 A 数组中的每一个数进行分组，并且分数不一定需要是整数。

示例:
输入:
A = [9,1,2,3,9]
K = 3
输出: 20
解释:
A 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20.
我们也可以把 A 分成[9, 1], [2], [3, 9].
这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.

"""

"""
dp[i][k]用于记录A数组前i个元素分成k段平均值和的最大值。
如果k == 1，dp[i][k] = sum[i] * 1.0 / i。代表着把前i个元素分成1段，平均值和的最大值就是自身的平均值
否则dp[i][k] = max(dp[i][k], dp[j][k - 1] + 1.0 * (sum[i] - sum[j]) / (i - j));//其中j∈[1, i)，
//整个表达式代表把前个元素分成k段最大值 = max(把前j个分成k - 1段，最后[j, i)单独看做一段计算的和)
"""


class Solution:
    def largestSumOfAverages(self, A, K):
        l = len(A)

        # 1. 存储和，以便于后面快速查找
        sum_dict = [0 for _ in range(l + 1)]
        for i in range(1, l + 1):
            sum_dict[i] = sum_dict[i - 1] + A[i - 1]
        print(sum_dict)

        # 2. dp
        dp = [[0 for _ in range(K + 1)] for _ in range(l + 1)]

        for i in range(1, l + 1):
            dp[i][1] = sum_dict[i] / i
            for k in range(2, K + 1):
                if k <= i:
                    for j in range(1, i):
                        dp[i][k] = max(dp[i][k], dp[j][k - 1] + (sum_dict[i] - sum_dict[j]) / (i - j))
        for i in dp:
            print(i)
        return dp[-1][-1]


if __name__ == '__main__':
    A = [9, 1, 2, 3, 9]
    K = 3
    print(Solution().largestSumOfAverages(A, K))
