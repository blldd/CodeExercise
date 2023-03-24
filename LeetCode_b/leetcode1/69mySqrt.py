# -*- coding: utf-8 -*-
"""
@Time    : 2019/10/9 10:36 PM
@Author  : ddlee
@File    : 69mySqrt.py
"""

"""
69. x 的平方根

实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
输入: 4
输出: 2

示例 2:
输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        low = 0
        high = x // 2 + 1

        while low < high:
            mid = (low + high + 1) >> 1
            # if mid * mid == x:
            #     return mid
            if mid * mid <= x:
                low = mid
            else:
                high = mid - 1
        return low

    def mySqrt1(self, x):
        if x < 0:
            raise Exception('不能输入负数')
        if x == 0:
            return 0
        # 起始的时候在 1 ，这可以比较随意设置
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)


if __name__ == '__main__':
    print(Solution().mySqrt(8))
