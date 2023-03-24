# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/19 9:00 PM
@Author  : ddlee
@File    : 279_numSquares.py
"""
import sys

'''
 
279. 完全平方数

给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:
输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.

示例 2:
输入: n = 13
输出: 2
解释: 13 = 4 + 9.
'''


class Solution:
    def numSquares(self, n: int) -> int:
        if n < 1:
            return 0

        dp = [sys.maxsize for i in range(n + 1)]
        dp[0] = 0

        rnd = int(pow(n, 0.5)) + 1

        for i in range(1, rnd):
            for j in range(pow(i, 2), n + 1):
                dp[j] = min(dp[j], dp[j - pow(i, 2)] + 1)

        # print(dp)
        return dp[-1]

    def numSquares1(self, n):
        """
        :type n: int
        :rtype: int
        """

        def help(N, size):
            if (N == 0): return True;
            if (size == 0): return False;
            k = int(pow(N, 0.5));
            for i in range(k, 0, -1):
                if (help(N - i * i, size - 1)):
                    return True
            return False

        f = False
        ans = 0;
        while (f == 0):
            ans = ans + 1;
            f = help(n, ans)
        return ans


if __name__ == '__main__':
    print(Solution().numSquares2(6175))
