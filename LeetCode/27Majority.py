# -*- coding:UTF-8 -*-

'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == num:
                count += 1
            else:
                count -= 1
                if count < 0:
                    num = nums[i]
                    count = 1

        return num


if __name__ == '__main__':
    print(Solution().majorityElement([1, 2, 1, 1]))
