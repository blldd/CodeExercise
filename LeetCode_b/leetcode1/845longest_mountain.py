# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/11 3:06 PM
@Author  : ddlee
@File    : 845longest_mountain.py
"""


class Solution():
    def longestMountain1(self, arr):
        """
        求数组中的最长山脉
            - B.length >= 3
            - 存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
        输入：[2,1,4,7,3,2,5]
        输出：5
        解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。
        """

        # j结尾的递增序列
        def lis(arr):
            length = len(arr)
            dp = [0 for i in range(length + 1)]
            for i in range(1, length + 1):
                for j in range(i, length + 1):
                    if arr[j - 1] > arr[i - 1]:
                        dp[j] = max(dp[i] + 1, dp[j])
            return dp

        # i开头的递减序列
        def lds(arr):
            length = len(arr)
            dp = [0 for i in range(length + 1)]
            for i in range(1, length + 1)[::-1]:
                for j in range(i, length + 1)[::-1]:
                    if arr[j - 1] < arr[i - 1]:
                        dp[i] = max(dp[j] + 1, dp[i])
            return dp

        lis_dp = lis(arr)
        print(lis_dp)
        lds_dp = lds(arr)
        print(lds_dp)

        res = []
        for i in range(len(lis_dp)):
            if lis_dp[i] and lds_dp[i]:
                res.append(lis_dp[i] + lds_dp[i] + 1)
            else:
                res.append(0)
        return max(res) if res else 0

    def longestMountain(self, arr):
        """
        求数组中的最长山脉
            - B.length >= 3
            - 存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
        输入：[2,1,4,7,3,2,5]
        输出：5
        解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。
        """

        # i结尾的递增序列
        def lis(arr):
            length = len(arr)
            dp = [0 for i in range(length)]
            for i in range(1, length):
                if arr[i] > arr[i - 1]:
                    dp[i] = max(dp[i - 1] + 1, dp[i])
            return dp

        # i开头的递减序列
        def lds(arr):
            length = len(arr)
            dp = [0 for i in range(length)]
            for i in range(length - 1)[::-1]:
                if arr[i] > arr[i + 1]:
                    dp[i] = max(dp[i + 1] + 1, dp[i])
            return dp

        lis_dp = lis(arr)
        # print(lis_dp)
        lds_dp = lds(arr)
        # print(lds_dp)

        res = []
        for i in range(len(lis_dp)):
            if lis_dp[i] and lds_dp[i]:
                res.append(lis_dp[i] + lds_dp[i] + 1)
            else:
                res.append(0)
        return max(res) if res else 0


if __name__ == '__main__':
    arr = [2, 1, 4, 7, 3, 2, 5]
    arr = list(range(5))
    arr = []
    print(Solution().longestMountain(arr))
