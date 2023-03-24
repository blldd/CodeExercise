# -*- coding:utf-8 -*-
"""

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases.

"""

"""采用除余结合的思想，但是要考虑26%26 为0，所以我们可以先对n-1，再除以26，再加上'A'，"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n:
            res = chr((n - 1) % 26 + ord('A')) + res
            n = (n - 1) / 26
        return res


if __name__ == '__main__':
    mat = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    num = 28
    print(Solution().convertToTitle(num))
    # print(dups)
    # print(arr)
