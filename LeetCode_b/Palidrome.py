"""
给一串字母，求可以组合的最长的回文长度
最长的回文数可以由三部分组成：
1、出现次数为偶数的，总长度增加其出现次数。
2、出现次数为奇数，但是大于1次的，此时总长度增加其出现次数-1次。
3、只要有出现次数为奇数的元素，总长度再加1。
"""

import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = collections.Counter(s)
        return sum([t[x] for x in t if t[x] %2==0]) + sum([t[x]-1 for x in t if t[x] > 1 and t[x]%2==1]) + max([1 for x in t if t[x]%2==1] or [0])

