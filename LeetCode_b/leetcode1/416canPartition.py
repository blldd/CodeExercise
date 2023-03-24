# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/10 11:02 AM
@Author  : ddlee
@File    : 416canPartition.py
"""

"""
416. 分割等和子集
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200

示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].
"""


class Solution:
    def canPartition(self, nums):
        _sum = sum(nums)

        # if _sum % 2 != 0:
        if _sum & 1 != 0:
            return False

        target = _sum >> 1


        tmp = 0
        while nums:
            node = nums.pop()
            tmp += node
            if tmp < target:
                continue
            elif tmp == target:
                return True
            else:
                tmp -= node
                nums.insert(0,  node)
        return False

    # 主要思想为：记录对nums取所有组合下可能出现的和，最后判断总和的一半是否在这些和中，其实还是动态规划
    # 以下实现进行了提前结束，迭代时的哈希判断等优化
    def canPartition1(self, nums):
        target, remain = divmod(sum(nums), 2)
        if remain:  # 如果不能整除直接返回
            return False
        ans = {0}
        for i in nums:
            for j in list(ans):  # 循环中会改变ans
                j += i
                if j == target:  # 提前结束
                    return True
                ans.add(j)  # 之前的结果加当前数能得到的结果
        return False



if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    nums = [18, 40, 62, 33, 83, 64, 10, 92, 67, 31, 42, 51, 10, 97, 41, 7, 82, 71, 80, 81, 41, 38, 88, 25, 38, 89, 24,
            89, 90, 12, 97, 21, 22, 85, 11, 59, 83, 6, 51, 47, 32, 82, 83, 100, 29, 78, 36, 32, 1, 31, 36, 19, 35, 3,
            36, 21, 24, 93, 42, 33, 10, 26, 2, 39, 36, 62, 85, 24, 41, 5, 66, 53, 7, 1, 59, 53, 40, 59, 41, 95, 7, 67,
            20, 29, 80, 59, 49, 49, 51, 90, 13, 52, 6, 90, 5, 6, 31, 81, 95, 26]
    print(Solution().canPartition1(nums))
