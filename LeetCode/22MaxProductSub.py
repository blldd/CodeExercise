# -*- coding:UTF-8 -*-

'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''



class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        positive_max = [0] * len(nums)
        negative_min = [0] * len(nums)

        if nums[0] > 0:
            positive_max[0] = nums[0]
        if nums[0] < 0:
            negative_min[0] = nums[0]

        for idx in range(1, len(nums)):
            num = nums[idx]
            if num > 0:
                positive_max[idx] = max(positive_max[idx - 1] * num, num)
                negative_min[idx] = negative_min[idx - 1] * num
            if num < 0:
                positive_max[idx] = negative_min[idx - 1] * num
                negative_min[idx] = min(positive_max[idx - 1] * num, num)

            print(positive_max)
            print(negative_min)
        return max(positive_max)


if __name__ == '__main__':
    nums = [3, -2, -5, 2, 0]
    print(Solution().maxProduct(nums))