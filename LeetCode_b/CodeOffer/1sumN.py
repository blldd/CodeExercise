# -*- coding:utf-8 -*-

"""
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""

class Solution:
    def Sum_Solution_1(self, n):
        # write code here
        return sum([i for i in range(n + 1)])

    def __init__(self):
        self.sum = 0

    def Sum_Solution(self, n):
        # write code here
        def sum_n(n):
            self.sum += n
            n -= 1
            return n > 0 and self.Sum_Solution(n)

        sum_n(n)
        return self.sum


if __name__ == '__main__':
    n = 10
    print(Solution().Sum_Solution(n))
