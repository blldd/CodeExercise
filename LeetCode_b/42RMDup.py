# -*- coding:UTF-8 -*-

'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        i = 0
        j = 0
        while i < n:
            while i < n-1 and nums[i] == nums[i+1]:
                i += 1
            nums[j] = nums[i]
            j += 1
            i += 1

        return j
    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        j = 0
        while i < n:
            if i < n-1 and nums[i] == nums[i+1]:
                i+=1
                continue
            j += 1
            i+=1

        return j

if __name__ == '__main__':
    nums = [1, 1, 2, 3, 4, 4, 5]
    print(Solution().removeDuplicates(nums))
    print(nums)
