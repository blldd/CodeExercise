# -*- coding:UTF-8 -*-

'''
Given a sorted array
[1,2,2,]

'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums is None:
            return 0
        for i in range(1, len(nums)):
            idx = 0
            if nums[i] != nums[idx]:
                idx = idx + 1
                nums[idx] = nums[i]
        return idx + 1



if __name__ == '__main__':
    nums = [1, 1, 2]
    target = 3
    print(Solution().removeDuplicates(nums))
