# -*- coding:UTF-8 -*-

'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

class Solution(object):

    def convert(self, s, numRows):

        if numRows < 2 or numRows >= len(s):
            return s

        zigzag = [[] for _ in range(numRows)]
        row, step = 0, 1
        for c in s:
            zigzag[row] += c
            if row == 0:
                step = 1
            if row == numRows - 1:
                step = -1
            row += step

        return "".join(map(lambda x: "".join(x), zigzag))



if __name__ == '__main__':

    print(Solution().convert("alnnwetmb", 3))

