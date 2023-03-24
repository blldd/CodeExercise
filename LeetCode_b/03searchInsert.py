# -*- coding:UTF-8 -*-

'''

'''


class Solution(object):
    def searchInsert1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if nums is None:
            return 0
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
        return left
if __name__ == '__main__':
    nums = [1, 1, 2]
    target = 1
    print(Solution().searchInsert(nums, 2))
