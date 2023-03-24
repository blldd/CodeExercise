# -*- coding:UTF-8 -*-

'''
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
'''


class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = bin(n)
        print(b)

        # 不到32位,变成32位
        if len(b) < 34:
            b = '0b' + '0' * (34 - len(b)) + b[2:]

        print(b)
        reversed_b = "0b" + b[2:][::-1]

        return int(reversed_b, 2)


if __name__ == '__main__':
    print(Solution().reverseBits(43261596))
