# -*- coding:UTF-8 -*-

class Solution(object):
    def convert(self, s, numRows):
        """
        将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
        输入: s = "LEETCODEISHIRING", numRows = 4
        输出: "LDREOEIIECIHNTSG"
        解释:

        L     D     R
        E   O E   I I
        E C   I H   N
        T     S     G
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        arr = [""] * numRows
        idx, step = 0, 1
        for ch in s:
            arr[idx] += ch
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1
            idx += step
        return "".join(arr)


if __name__ == '__main__':
    print(Solution().convert("LEETCODEISHIRING", 4))

