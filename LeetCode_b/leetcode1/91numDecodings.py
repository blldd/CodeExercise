# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/12 9:09 AM
@Author  : ddlee
@File    : 91numDecodings.py
"""


class Solution:
    def numDecodings1(self, s: str) -> int:
        if s and "0" == s[0]:
            return 0
        if len(s) < 1:
            return 1
        if len(s) == 1:
            return 1
        if int(s[:2]) < 27:
            return self.numDecodings1(s[1:]) + self.numDecodings1(s[2:])
        return self.numDecodings1(s[1:])

    def numDecodings(self, s):
        # case 00001
        if s and "0" == s[0]:
            return 0
        if len(s) <= 1:
            return 1
        l = len(s)
        dp = [1 for _ in range(l + 1)]
        for i in range(2, l + 1):
            if s[i - 2] != "0":
                num = int(s[i - 2:i])
                if num < 27 and num > 0:
                    # 10 20
                    if s[i - 1] == "0":
                        dp[i] = dp[i - 2]
                    else:
                        dp[i] = dp[i - 1] + dp[i - 2]
                elif s[i - 1] != "0":
                    dp[i] = dp[i - 1]
                else:
                    return 0
            elif s[i - 1] != "0":
                dp[i] = dp[i - 2]
            else:
                return 0
        print(dp)
        return dp[-1]


if __name__ == '__main__':
    s = "27"
    # 2226   2 2 2 6 | 2 2 26 | 22 2 6 | 2 22 6 | 22 26
    s = "9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"
    # s = "10"

    print(Solution().numDecodings(s))
    print(Solution().numDecodings1(s))
