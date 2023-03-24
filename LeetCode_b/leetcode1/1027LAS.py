# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/23 10:45 PM
@Author  : ddlee
@File    : 1027LAS.py
"""


class Solution:
    """
    输入：[3,6,9,12]
    输出：4
    解释：
    整个数组是公差为 3 的等差数列。
    """
    '''加缓存'''
    def longestArithSeqLength(self, A) -> int:
        if A == None or A == []:
            return 0

        n, res = len(A), 1
        dp = [{0: 1} for _ in range(n)]

        for j in range(n):
            for i in range(j):
                step = A[j] - A[i]
                if step in dp[i]:
                    if step in dp[j]:
                        dp[j][step] = max(dp[i][step] + 1, dp[j][step])
                    else:
                        dp[j][step] = dp[i][step] + 1
                else:
                    dp[j][step] = 2
            res = max(res, max(dp[j].values()))

        print(dp)
        return res

    '''暴力超时'''
    def las(self, A):
        if A == None or A == []:
            return 0

        l = len(A)
        if l < 2:
            return l

        res = 2
        for i in range(l):
            for j in range(i + 1, l):
                tmp = 2
                gap = A[j] - A[i]
                next = A[j] + gap
                for k in range(j + 1, l):
                    if A[k] == next:
                        tmp += 1
                        next += gap
                res = max(res, tmp)
        return res


if __name__ == '__main__':
    A = [61,41,59,7,40,46,7,37,70,32,49,58,8,37,59,32,70,53,3,28,17,3,4,66,44,54,6,17,21,70,8,30,28,48,62,13,16,59,47,23,67,26,55,55,71,4,72,51,49,44,59,46,5,0,7,40,67,9,1,39,40,35,47,30,63,49,7,45,47,7,11,3,12,38,72,65,53,5,33,47,67,34,15,4,35,38,53,13,45,23,0,5,62,58,35,6,33,77,30,75]
    print(Solution().longestArithSeqLength(A))
