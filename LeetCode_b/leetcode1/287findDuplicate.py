# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/1 9:56 PM
@Author  : ddlee
@File    : 287findDuplicate.py
"""

"""
287. 寻找重复数
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:
输入: [1,3,4,2,2]
输出: 2

示例 2:
输入: [3,1,3,4,2]
输出: 3

说明：
不能更改原数组（假设数组是只读的）。!!!
只能使用额外的 O(1) 的空间。!!!
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。
"""


class Solution:
    # wrong
    def findDuplicate1(self, nums):
        l = len(nums)
        _max = 0
        _min = float('inf')

        for i in nums:
            if i > _max:
                _max = i
            if i < _min:
                _min = i

        if _min == _max:
            return _min

        n = _max - _min + 1

        return (sum(nums) - (_max + _min) * n // 2) // (l - n)

    # right
    def findDuplicate(self, nums):
        # l = len(nums)
        _max = max(nums)

        left = 0
        right = _max
        while left < right:
            mid = (left + right) // 2

            cnt = 0
            for i in nums:
                if i <= mid:
                    cnt += 1
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid
        return left

    # 快慢指针法
    """
    使用数组中的值作为索引下标进行遍历，遍历的结果肯定是一个环（有一个重复元素） 
    检测重复元素问题转换成检测环的入口 为了找到环的入口，可以进行如下步骤：
    
    设置两个快慢指针， fast每次走两步，slow每次走一步，最终走了slow走了n步与fast相遇，fast走了2*n，fast可能比slow多饶了环的i圈，得到环的周长为n/i
    slow指针继续走, 且另设第三个指针每次走一步，两个指针必定在入口处相遇
    假设环的入口和起点的距离时m
    当第三个指针走了m步到环的入口时
    slow刚好走了n + m步，换句话说时饶了环i圈（环的周长为n/i）加m步（起点到入口的距离）
    得到相遇的是环的入口，入口元素即为重复元素
    """
    def findDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, second = 0, 0
        while True:
            second = nums[second]
            first = nums[nums[first]]
            if first == second:
                break
                # 值相等的两个下标

        # 快的置零，慢的停在乌龟，重新开始跑，每次跑一步
        ptr1 = 0
        ptr2 = second
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        return ptr1


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    # nums = [1, 2, 2, 2, 2]
    # nums = [1, 4, 4, 2, 4]

    print(Solution().findDuplicate(nums))
    print(Solution().findDuplicate2(nums))
