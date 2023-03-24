# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/8 8:15 PM
@Author  : ddlee
@File    : 41firstMissingPositive.py
"""

"""
41. 缺失的第一个正数
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:
输入: [1,2,0]
输出: 3

示例 2:
输入: [3,4,-1,1]
输出: 2

示例 3:
输入: [7,8,9,11,12]
输出: 1

说明:
你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间！！！
"""

"""
此题目可以做个推广 leetcode268题！！！推广到缺失k个数
解法：
用此题目解法，找出第一个，补上，找第二个，补上，第k个。。。。

桶排序思想
"""


class Solution:
    def firstMissingPositive1(self, nums):
        l = len(nums)

        queue = nums[::-1].copy()
        while queue:
            node = queue.pop()
            if node > 0 and node <= l:
                tmp = nums[node - 1]
                if tmp != node and tmp <= l:
                    queue.append(tmp)

            if node > 0 and node <= l:
                nums[node - 1] = node

        for idx, num in enumerate(nums):
            if num - 1 != idx:
                return idx + 1
        return l + 1

    def firstMissingPositive(self, nums):
        size = len(nums)
        if size == 0:
            return 1

        for i in range(size):
            while nums[i] > 0 and nums[i] <= size:
                if nums[nums[i] - 1] == nums[i]:
                    # 如果已经在合适的位置上，就不用交换了
                    break
                # 这里我单独把交换数组两个位置的方法封装起来，是为了不让自己出错，这一行代码有点绕
                # 就要把它放到合适的位置上，i 应该放在索引为 i - 1 的位置上
                self.__swap(nums, i, nums[i] - 1)

        # 从头到尾看一遍
        for i in range(size):
            if nums[i] != i + 1:
                return i + 1
        return size + 1

    def __swap(self, nums, index1, index2):
        if index1 == index2:
            return
        nums[index1], nums[index2] = nums[index2], nums[index1]

    def __swap1(self, nums, index1, index2):
        """
        交换trick：
        a = a ^ b
        b = a ^ b
        a = a ^ b
        """
        # nums[index1], nums[index2] = nums[index2], nums[index1]
        nums[index1] = nums[index1] ^ nums[index2]
        nums[index2] = nums[index1] ^ nums[index2]
        nums[index1] = nums[index1] ^ nums[index2]


if __name__ == '__main__':
    nums = [3, 4, -1, 1]
    # nums = [7, 8, 9, 11, 12]
    # nums = [1]
    # nums = []
    nums = [3, 4, 2, 5]

    print(Solution().firstMissingPositive(nums))
