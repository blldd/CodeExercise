# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/15 7:05 PM
@Author  : ddlee
@File    : 392isSubsq.py
"""


class Solution:
    def isSubsequence1(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        return i == len(s)


if __name__ == '__main__':
    s = "acb"
    t = "ahbgdc"
    print(Solution().isSubsequence(s, t))