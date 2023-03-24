# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/8 6:00 PM
@Author  : ddlee
@File    : 268missingNumber.py
"""
"""
268. 缺失数字
==》287 
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:
输入: [3,0,1]
输出: 2

示例 2:
输入: [9,6,4,2,3,5,7,0,1]
输出: 8
"""


class Solution:
    def missingNumber1(self, nums):
        l = len(nums)
        _sum = l * (l + 1) // 2
        return _sum - sum(nums)

    def missingNumber(self, nums):
        l = len(nums)

        def get_num(le, ri, nums):
            cnt = 0
            for num in nums:
                if num >= le and num <= ri:
                    cnt += 1
            return cnt

        left = 0
        right = l
        while left < right:
            mid = (left + right) // 2
            cnt = get_num(left, mid, nums)
            if cnt < mid - left + 1:
                right = mid
            elif cnt == mid - left + 1:
                left = mid + 1
        return left

    def missingNumber_xor(self, nums):
        l = len(nums)

        res = l
        for i, num in enumerate(nums):
            res ^= i ^ num

        return res

if __name__ == '__main__':
    nums = [3, 0, 1]
    # nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    # nums = [0, 2]

    print(Solution().missingNumber_xor(nums))
