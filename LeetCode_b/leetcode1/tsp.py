# -*- coding:UTF-8 -*-
import sys


class Solution(object):
    def get_min_cost(self, a):
        n = len(a)
        bits = [1 << i for i in range(n)]
        d = [[-1 for j in range(1000)] for i in range(n)]
        t = 1
        for i in range(1, n):
            d[t << (i - 1)][i] = a[0][i]
        res = sys.maxsize
        t = 0
        for i in range(1, n):
            t <<= 1
            t |= 1
        for i in range(1, n):
            r = self.getD(i, t, n, a, bits, d)
            if r + a[i][0] < res:
                res = r + a[i][0]
        return res

    def getD(self, i, t, n, a, bits, d):
        _min = -sys.maxsize - 1
        if d[t][i] != -1:
            return d[t][i]
        t &= (~bits[i - 1])
        for j in range(1, n):
            tt = t & bits[j - 1]
            if tt > 0:
                res = self.getD(j, t, n, a, bits, d)
                _min = min(_min, res + a[j][i])
        d[t][i] = _min
        return d[t][i]


if __name__ == '__main__':
    a = [[0, 3, 6, 7],
         [5, 0, 2, 3],
         [6, 4, 0, 2],
         [3, 7, 5, 0]]
    print(Solution().get_min_cost(a))
