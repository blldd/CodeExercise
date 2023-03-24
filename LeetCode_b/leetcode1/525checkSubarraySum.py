# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/20 7:14 PM
@Author  : ddlee
@File    : 525checkSubarraySum.py
"""

"""
523. 连续的子数组和

给定一个包含非负数的数组和一个目标整数 k
编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，总和为 k 的倍数，即总和为 n*k，其中 n 也是一个整数。

示例 1:
输入: [23,2,4,6,7], k = 6
输出: True
解释: [2,4] 是一个大小为 2 的子数组，并且和为 6。

示例 2:
输入: [23,2,6,4,7], k = 6
输出: True
解释: [23,2,6,4,7]是大小为 5 的子数组，并且和为 42。
"""


class Solution:
    def checkSubarraySum(self, arr, target: int) -> bool:
        l = len(arr)
        if l < 1:
            return False

        for i in range(l):
            for j in range(i + 2, l + 1):
                tmp = sum(arr[i:j])
                if target == tmp:
                    return True

                if target != 0 and tmp % target == 0:
                    return True

        return False


if __name__ == '__main__':
    arr = [23,2,6,4,7]

    k = 0

    print(Solution().checkSubarraySum(arr, k))
