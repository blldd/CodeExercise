# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/29 10:11 PM
@Author  : ddlee
@File    : 38countAndSay.py
"""

"""
38. 报数
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。

示例 1:
输入: 1
输出: "1"

示例 2:
输入: 4
输出: "1211"
"""


class Solution:
    def countAndSay(self, n):
        if n < 1:
            return ""
        if n == 1:
            return "1"

        def split_str(num_str):
            arr = []
            tmp = num_str[0]
            for i in num_str[1:]:
                if i == tmp[-1]:
                    tmp += i
                else:
                    arr.append(tmp)
                    tmp = i
            arr.append(tmp)
            return arr

        def translate2num(arr):
            num_str = ""
            for i in arr:
                s = str(len(i)) + str(i[0])
                num_str += s
            return num_str

        # arr = split_str("111221")
        # print(arr)
        num_str = "1"
        for i in range(1, n):
            arr = split_str(num_str)
            num_str = translate2num(arr)
        return num_str


    def countAndSay1(self, n):
        """
        :type n: int
        :rtype: str
        """
        last = "1"
        for i in range(1, n):
            now = ""
            cnt = 0
            for j in range(len(last)):
                cnt += 1
                if j == (len(last) - 1) or (last[j] != last[j+1]):
                    now += str(cnt) + last[j]
                    cnt = 0
            last = now
        return last

if __name__ == '__main__':
    n = 4
    print(Solution().countAndSay(n))
