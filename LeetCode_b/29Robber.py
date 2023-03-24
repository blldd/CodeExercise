# -*- coding:UTF-8 -*-

'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]
        if nums == []:
            return 0

        dp = [None] * len(nums)

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for idx in range(2, len(nums)):
            dp[idx] = max(dp[idx - 1], dp[idx - 2] + nums[idx])

        return dp[-1]


if __name__ == '__main__':
    print(Solution().rob([1, 4, 9, 7, 1, 2, 39999944, 5, 5]))