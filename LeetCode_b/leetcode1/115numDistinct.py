# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/25 2:17 PM
@Author  : ddlee
@File    : 115numDistinct.py
"""

"""
不同的子序列
给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。
一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。
（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

示例 1:

输入: S = "rabbbit", T = "rabbit"
输出: 3
解释:
如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ls = len(s) + 1
        lt = len(t) + 1

        dp = [[0 for j in range(lt)] for i in range(ls)]
        if not t:
            return 1
        for i in range(ls):
            dp[i][0] = 1
            dp[i][1] = s[:i].count(t[0])

        for i in range(1, ls):
            for j in range(1, lt):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                    # 相等的情况：s用相等这一位的方案 +  s不用相等这一位的方案
                else:
                    dp[i][j] = dp[i - 1][j]
        for i in dp:
            print(i)
        return dp[-1][-1]


if __name__ == '__main__':
    s = "rabbbit"
    t = "rabbit"
    print(Solution().numDistinct(s, t))
