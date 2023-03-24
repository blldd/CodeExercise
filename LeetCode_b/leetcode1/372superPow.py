# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/15 7:31 PM
@Author  : ddlee
@File    : 372superPow.py
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return pow(x, n)
        i = n
        if i < 0:
            i = -i

        res = 1
        while i != 0:
            if i % 2 != 0:
                res *= x
            x *= x
            i = i // 2
        return res if n > 0 else 1 / res

    def superPow(self, a, b):
        """
        你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。

        示例 1:
        输入: a = 2, b = [3]
        输出: 8
        示例 2:

        输入: a = 2, b = [1,0]
        输出: 1024
        """
        def modn(a, b, c):
            res = 1
            while b != 0:
                if (b & 1):
                    res *= a
                    res %= c
                a *= a
                a %= c
                b >>= 1
            return res

        power = 0
        for i in b:
            power = power * 10 + i
        a = a % 1337
        res = modn(a, power, 1337)
        return res % 1337


if __name__ == '__main__':
    a = 2
    b = [3, 0, 0]
    print(Solution().superPow(a, b))
