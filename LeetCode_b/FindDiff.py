

"""

"""
import operator
from functools import reduce


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(reduce(operator.xor, map(ord, (s + t))))

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = dict()
        for single in s:
            dic[single] = dic.get(single, 0) + 1
        for single in t:
            if single in dic:
                dic[single] = dic[single] - 1
                if dic[single] == 0:
                    del dic[single]
            else:
                return single

