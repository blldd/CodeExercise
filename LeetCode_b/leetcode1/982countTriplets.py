# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/14 9:31 AM
@Author  : ddlee
@File    : 982countTriplets.py
"""
import collections


class Solution:
    """
    给定一个整数数组 A，找出索引为 (i, j, k) 的三元组，使得：

    0 <= i < A.length
    0 <= j < A.length
    0 <= k < A.length
    A[i] & A[j] & A[k] == 0，其中 & 表示按位与（AND）操作符。
    """

    def countTriplets_naive(self, A):
        l = len(A)
        cnt = 0
        for i in range(l):
            for j in range(l):
                for k in range(l):
                    if A[i] & A[j] & A[k] == 0:
                        cnt += 1
        return cnt

    """
    ******- 时间复杂度: O(N^3)******- 空间复杂度: O(N^2)******
    想到用counter，然后先确定一下A中每一对元素的AND的结果一共有多少种，每种各自有多少个，然后重新遍历我们的A，对于每一个元素a
    看看count里面有哪一个AND结果and_res和a的AND为0，加上这个and_res的频率即可
    
    worst case 如下：
    maybe each pair of elements in original A will have a different AND result, 
    therefore, the count can have O(N^2) elements in the worst case.
    
    空间最差为O(N^2)
    """

    def countTriplets(self, A: 'List[int]') -> 'int':
        res = 0
        count = collections.Counter()

        for i in range(len(A)):
            for j in range(len(A)):
                count[A[i] & A[j]] += 1

        for k in range(len(A)):
            for v in count:
                if A[k] & v == 0:
                    res += count[v]
        return res


if __name__ == '__main__':
    A = [2, 1, 3]
    print(Solution().countTriplets(A))
