# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/27 7:16 PM
@Author  : ddlee
@File    : 303sumRange.py
"""

"""
303. 区域和检索 - 数组不可变
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：
给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

说明:
你可以假设数组不可变。
会多次调用 sumRange 方法。
"""


# class NumArray:
#
#     def __init__(self, nums):
#         self.nums = nums
#
#     def sumRange(self, i, j):
#         return sum(self.nums[i:j + 1])

class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.sum_n = [0]

        l = len(nums)
        for i  in range(l):
            self.sum_n.append(self.sum_n[i]+self.nums[i])
        # print(self.sum_n)

    def sumRange(self, i, j):
        return self.sum_n[j+1] - self.sum_n[i]


if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    param_1 = obj.sumRange(2, 5)
    print(param_1)
