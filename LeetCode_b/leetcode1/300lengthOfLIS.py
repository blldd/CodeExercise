# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/17 9:11 AM
@Author  : ddlee
@File    : 300lengthOfLIS.py
"""
import sys

"""
300. 最长上升子序列
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

说明:
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?


"""
class Solution:

    def lengthOfLIS(self, nums) -> int:
        l = len(nums)
        if l < 2:
            return l

        tail = [sys.maxsize]

        for num in nums:
            # 找到大于等于 num 的第 1 个数
            # 经典二分查找
            le = 0
            ri = len(tail)
            while le < ri:
                mid = le + (ri - le) // 2
                if tail[mid] < num:
                    le = mid + 1
                else:
                    ri = mid

            if le == len(tail):
                tail.append(num)
            else:
                tail[le] = num

        print(tail)
        return len(tail)

    def lengthOfLIS_dp1(self, nums) -> int:
        l = len(nums) + 1

        dp = [1 for i in range(l)]
        dp[0] = 0
        for i in range(1, l):
            for j in range(i, l):
                if nums[i - 1] < nums[j - 1]:
                    dp[j] = max(dp[i] + 1, dp[j])
        print(dp)
        return max(dp)
    
    def lengthOfLIS_dp2(self, nums) -> int:
        n = len(nums)
        if n < 2:
            return n

        dp = [1] * n
        for i in range(n)[::-1]:
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        return max(dp)

    def lengthOfLIS_dp3(self, nums) -> int:
        n = len(nums)
        if n < 2:
            return n

        dp = [1] * n
        for i in range(n):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)
        print(dp)
        return max(dp)

if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    # nums = [4, 10, 4, 3, 8, 9]
    nums = [1, 3, 5, 4, 7]
    # nums = [2, 2, 2, 2, 2]

    print(Solution().lengthOfLIS_dp3(nums))
