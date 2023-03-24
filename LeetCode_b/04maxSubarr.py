# -*- coding:UTF-8 -*-

'''
[-2, 1, 3, 4, -1, 2, 1, -5]
'''


class Solution(object):
    def maxSubArray(self, nums):
        if nums is None:
            return 0
        maxCur = maxSoFar = nums[0]
        for i in range(1, len(nums)):
            maxCur += nums[i]
            maxCur = max(nums[i], maxCur)
            maxSoFar = max(maxCur, maxSoFar)
        return maxSoFar


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5]
    print(Solution().maxSubArray(nums))
