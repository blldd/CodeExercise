# -*- coding: utf-8 -*-
"""
@Time    : 2019/4/22 9:05 PM
@Author  : ddlee
@File    : 470rand10.py
"""
import random


class Solution:
    def rand10(self, n):
        """
        :rtype: int
        """

        def rand7():
            return random.randint(1, 7)
        res = []
        for i in range(n):
            x = 7 * (rand7() - 1) + rand7()
            while x > 40:
                x = 7 * (rand7() - 1) + rand7()
            rnd = x % 10 + 1
            res.append(rnd)
        return res


if __name__ == '__main__':
    n = 1000000
    res = Solution().rand10(n)
    cnt = [0 for i in range(10)]
    for i in res:
        cnt[i-1] += 1
    print(cnt)
