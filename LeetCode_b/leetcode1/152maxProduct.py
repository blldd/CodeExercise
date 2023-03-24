# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/26 10:13 AM
@Author  : ddlee
@File    : 152maxProduct.py
"""


class Solution:
    def maxProduct(self, nums):
        l = len(nums)
        if l == 1:
            return nums[0]

        dp = [[1, 1] for i in range(l + 1)]

        for i in range(1, l + 1):
            dp[i][0] = max(nums[i - 1], nums[i - 1] * dp[i - 1][0], nums[i - 1] * dp[i - 1][1])
            dp[i][1] = min(nums[i - 1], nums[i - 1] * dp[i - 1][0], nums[i - 1] * dp[i - 1][1])
        print(dp)
        ma = [item[0] for item in dp]
        mi = [item[1] for item in dp]
        print(ma)
        print(mi)
        return (max(ma[1:]))


if __name__ == '__main__':
    nums = [2, 3, -2, -4, -2, 4]
    print(Solution().maxProduct(nums))
