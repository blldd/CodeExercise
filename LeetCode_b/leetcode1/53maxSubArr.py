# -*- coding:UTF-8 -*-
import sys


class Solution(object):
    def maxSubArray(self, nums):
        """
        给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
        输入: [-2,1,-3,4,-1,2,1,-5,4],
        输出: 6
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return sum(nums)

        max_sum = -sys.maxsize    # 最终的最大值
        last_sum = -sys.maxsize   # 到现在为止的最大的序列和
        for i in nums:
            if last_sum < 0:
                last_sum = i
            else:
                last_sum += i

            max_sum = max(max_sum, last_sum)
        return max_sum

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # 到现在为止的最大的序列和，是一个dp问题，每一个最大和依赖于前一种状态，
    # -2 1 -2 4 3 5 6
    print(Solution().maxSubArray(nums))
