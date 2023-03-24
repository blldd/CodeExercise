# -*- coding: utf-8 -*-
# @ 2019-07-20
# @ Li Dedong
"""
34. 在排序数组中查找元素的第一个和最后一个位置

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""


class Solution:
    def searchRange(self, nums, target):
        def left_bound(nums, target):
            l = 0
            r = len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid
                else:
                    r = mid
            return l

        def right_bound(nums, target):
            l = 0
            r = len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1
            if r == 0:
                return -1
            return r - 1 if nums[l - 1] == target else -1

        if not nums or target < nums[0] or target > nums[-1]:
            return [-1, -1]

        left = left_bound(nums, target)
        right = right_bound(nums, target)
        # print(left, right)
        if left == -1 or right == -1:
            return [-1, -1]
        return [left, right]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 8, 8, 10]
    target = 8
    print(Solution().searchRange(nums, target))
