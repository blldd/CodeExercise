# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/8 6:00 PM
@Author  : ddlee
@File    : 268missingNumberII.py
"""
"""
268. 缺失两个数字
==》287 
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:
输入: [3,0,0]
输出: 1, 2

示例 2:
输入: [9,6,4,2,3,5,7,0,0]
输出: 8, 1
"""


class Solution:
    def find_missing_2_numbers(self, sequence):
        """ returns the missing two numbers of sequence, which is supposed
        to be a permutation of {1,..,n} with two numbers missing.
        """
        n =  len(sequence)
        x = n
        for i, e in enumerate(sequence):
            x ^= e ^ i
        diff = x & (-x)  # isolates the rightmost 1-bit
        a, b = 0, 0
        for i in range(1, n + 1):
            if i & diff:
                a ^= i
            else:
                b ^= i

        for e in sequence:
            if e & diff:
                a ^= e
            else:
                b ^= e
        return a, b


if __name__ == '__main__':
    nums = [3, 0, 0]
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 0]
    # nums = [0, 0]

    print(Solution().find_missing_2_numbers(nums))
