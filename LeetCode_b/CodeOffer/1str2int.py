# -*- coding:utf-8 -*-

"""
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，
但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。
数值为0或者字符串不是一个合法的数值则返回0。
"""


class Solution:
    def StrToInt(self, s):
        # write code here
        res = 0
        tag = 1
        arr = [str(i) for i in range(10)]
        for i in s:
            if i == '+':
                tag = 1
                continue
            if i == "-":
                tag = -1
                continue
            if i not in arr:
                return 0
            res = res * 10 + int(i)
        return res * tag


if __name__ == '__main__':
    str1 = ""
    print(Solution().StrToInt(str1))
