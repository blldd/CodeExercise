# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/18 10:27 PM
@Author  : ddlee
@File    : 139wordBreak.py
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 求字典中最长字符串
        maxlen = 0
        for word in wordDict:
            if len(word) > maxlen:
                maxlen = len(word)

        res = [0] * len(s)
        for i in range(len(s)):
            p = i
            while (p >= 0 and i - p <= maxlen):
                # 两个条件
                if (res[p] == 1 and s[p + 1:i + 1] in wordDict) or (p == 0 and s[p:i + 1] in wordDict):
                    res[i] = 1
                    break
                p -= 1

        print(res)
        return res[-1] == 1

    def word(self, s, wordDict):
        l = len(s)
        dp = [0 for _ in range(l)]

        if not wordDict:
            return False
        max_len = max(list(map(len, wordDict)))

        for i in range(l):
            p = i
            while p >= 0 and i - p <= max_len:
                if (dp[p] == 1 and s[p + 1:i + 1] in wordDict) or (p == 0 and s[p:i + 1] in wordDict):
                    dp[i] = 1
                    break
                p -= 1

        print(dp)
        return dp[-1] == 1


if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    s = 'a'
    wordDict = []
    s  = "dcacbcadcad"
    wordDict = ["cbd", "dca", "bcdc", "dcac", "ad"]
    print(Solution().word(s, wordDict))
