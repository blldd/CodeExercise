# -*- coding:UTF-8 -*-

'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
'''



class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        ans = ''
        while n:
            ans = chr(ord('A') + int((n - 1) % 26)) + ans
            n = int((n - 1) / 26)
        return ans


if __name__ == '__main__':
    print(Solution().convertToTitle(799))