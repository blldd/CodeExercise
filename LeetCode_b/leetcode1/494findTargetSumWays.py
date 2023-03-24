# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/30 9:41 AM
@Author  : ddlee
@File    : 494findTargetSumWays.py
"""

"""
494. 目标和

给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。
对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例 1:
输入: nums: [1, 1, 1, 1, 1], S: 3
输出: 5
解释: 
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
一共有5种方法让最终目标和为3。
"""


class Solution:
    def findTargetSumWays2(self, nums, S):
        '''2维'''
        su = sum(nums)
        if S > su:
            return 0
        l = len(nums)

        dp = [[0 for j in range(2 * su + 1)] for i in range(l)]
        dp[0][su + nums[0]] += 1
        dp[0][su - nums[0]] += 1
        for i in range(1, l):
            for j in range(2 * su + 1):
                if dp[i - 1][j] != 0:
                    dp[i][j - nums[i]] += dp[i - 1][j]
                    dp[i][j + nums[i]] += dp[i - 1][j]
                    # dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]
        for i in dp:
            print(i)
        # print(sum(dp[-1]))
        return dp[-1][su + S]

    def findTargetSumWays(self, nums, S):
        '''1维'''
        su = sum(nums)
        if S > su:
            return 0
        l = len(nums)

        dp = [0 for j in range(2 * su + 1)]
        dp_new = [0 for j in range(2 * su + 1)]
        dp[su + nums[0]] += 1
        dp[su - nums[0]] += 1
        for i in range(1, l):
            for j in range(2 * su + 1):
                if dp[j] != 0:
                    dp_new[j - nums[i]] += dp[j]
                    dp_new[j + nums[i]] += dp[j]
            dp = dp_new.copy()
            dp_new = [0 for j in range(2 * su + 1)]
        print(dp)
        return dp[su + S]

    def findTargetSumWaysTest(self, nums, S):
        if S > sum(nums):
            return 0
        l = len(nums)

        dp = [[0 for j in range(21)] for i in range(l)]
        dp[0][10 + nums[0]] += 1
        dp[0][10 - nums[0]] += 1
        for i in range(1, l):
            for j in range(nums[i], 21 - nums[i]):
                dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]
        for i in dp:
            print(i)
        return dp[-1][10 + S]


if __name__ == '__main__':
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 1]
    S = 1
    print(Solution().findTargetSumWays(nums, S))

    
