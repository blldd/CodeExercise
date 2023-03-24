# -*- coding:UTF-8 -*-

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        length = len(str)
        if length == 0:
            return 0

        pos = True
        if str[0] == "+" or str[0] == "-":
            if str[0] == "-":
                pos = False
            str = str[1:]

        n = 0
        for ch in str:
            if ch >=  '0' and ch <= '9':
                n = n * 10 + ord(ch) - ord('0')
            else:
                break

        if n > 2147483647:
            if pos:
                return 2147483648
            else:
                return -2147483647
        if not pos:
            return -n
        return n

if __name__ == '__main__':
    print(Solution().myAtoi("-91283472332"))