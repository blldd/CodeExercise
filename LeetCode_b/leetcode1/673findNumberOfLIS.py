# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/31 10:00 PM
@Author  : ddlee
@File    : 673findNumberOfLIS.py
"""
import collections
import sys

"""
673. 最长递增子序列的个数

给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:
输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。

示例 2:
输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
"""


class Solution:
    """
    记录每个位置 i 放数字num时的递增序列个数 dic[i][num]。
    当数字 newnum 放在 i+1 位置时，dic[i+1][newnum] 的值为 dic[i] 中 小于newnum 的num 的序列个数之和。
    """

    def findNumberOfLIS(self, nums):
        l = len(nums)
        if l < 2:
            return l

        cnt_arr = [collections.defaultdict(int)]

        tail = [sys.maxsize]
        for num in nums:
            # 找到大于等于 num 的第 1 个数
            # 经典二分查找
            le = 0
            ri = len(tail)
            while le < ri:
                mid = le + (ri - le) // 2
                if tail[mid] >= num:
                    ri = mid
                else:
                    le = mid + 1

            if le == len(tail):
                tail.append(num)

                tmp_dict = cnt_arr[-1]
                tmp = 0
                for k, v in tmp_dict.items():
                    if k < num:
                        tmp += v
                cnt_arr.append(collections.defaultdict(int))
                cnt_arr[-1][num] = tmp

            else:
                tail[le] = num

                # 之前没有
                if cnt_arr[le][num] == 0:
                    cnt_arr[le][num] += 1
                #
                elif le == len(tail) - 1:
                    cnt_arr[le][num] += 1

        print(tail)
        print(cnt_arr)
        last_sort = sorted(cnt_arr[-1].items(), key=lambda x: x[1], reverse=True)

        return max(last_sort[0][1], len(last_sort))


if __name__ == '__main__':
    nums = [1, 3, 5, 4, 7]
    nums = [2, 2, 2, 2, 2]
    # nums = [1, 2, 4, 3, 5, 4, 7, 2]
    # nums = [2, 1]
    # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1]
    nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    print(Solution().findNumberOfLIS(nums))
