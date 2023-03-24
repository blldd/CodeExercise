# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/11 3:55 PM
@Author  : ddlee
@File    : 525findMaxLength.py
"""
import sys

"""
525. 连续数组

给定一个二进制数组, 找到含有相同数量的 0 和 1 的最长连续子数组（的长度）。

示例 1:
输入: [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。

示例 2:
输入: [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
"""


class Solution:

    # 超时
    def findMaxLength_(self, nums):
        l = len(nums)

        sum_list = [0 for _ in range(l + 1)]
        for idx, num in enumerate(nums):
            sum_list[idx + 1] = sum_list[idx] + num
        # print(sum_list)

        ans = 0
        for i in range(1, l + 1):
            for j in range(i + 1, l + 1, 2):
                span = j - i + 1
                if span & 1 == 0 and sum_list[j] - sum_list[i - 1] == span >> 1:
                    ans = max(ans, span)

        return ans

    def findMaxLength2(self, nums):
        l = len(nums)
        if l <= 1:
            return 0

        zeros = 0
        ones = 0
        diff_dic = {0: -1}
        ans = 0
        for i, num in enumerate(nums):
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            diff = zeros - ones
            diff_dic[diff] = diff_dic.get(diff, i)
            ans = max(ans, i - diff_dic[diff])
        return ans


if __name__ == '__main__':
    nums = [0, 1, 0, 0, 1, 0, 0, 1]
    # nums = [1, 1, 1, 1, 1, 1, 1, 1]

    print(Solution().findMaxLength2(nums))
