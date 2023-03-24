# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/30 7:19 PM
@Author  : ddlee
@File    : 213rob.py
"""
"""
213. 打家劫舍 II

你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。
这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:
输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

示例 2:
输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
"""

class Solution:
    def rob(self, nums):
        def _rob(nums):
            l = len(nums)
            # rob i
            dp1 = [0 for _ in range(l)]
            # not rob i
            dp2 = [0 for _ in range(l)]

            for i in range(l):
                dp1[i] = max(dp1[i - 1], dp2[i - 1] + nums[i])
                dp2[i] = max(dp2[i - 1], dp1[i - 1])

            print(dp1)
            print(dp2)
            return dp1[-1]

        l = len(nums)
        if l < 1:
            return 0
        if l <= 3:
            return max(nums)

        rob_first = _rob(nums[:l-1])
        not_rob_first = _rob(nums[1:])

        return max(rob_first, not_rob_first)



if __name__ == '__main__':
    nums = [2,3,2]
    # nums = [1,2,3,1]
    # nums = [2,1,1,2]

    print(Solution().rob(nums))

