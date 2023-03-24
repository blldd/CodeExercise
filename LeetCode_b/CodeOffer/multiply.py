# -*- coding:utf-8 -*-

"""
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
不能使用除法。
"""


class Solution:
    def multiply(self, A):
        # write code here
        B = [0] * len(A)
        tmp = 1
        for i in range(len(A)):
            tmp *= A[i]

        for i in range(len(A)):
            if A[i] == 0:
                sp = 1
                for j in range(i):
                    sp *= A[j]
                for j in range(i+1, len(A)):
                    sp *= A[j]
                B[i] = sp
            else:
                B[i] = tmp / A[i]
        return B

    def multiply1(self, A):
        if not A:
            return []
        B = [0] * len(A)
        B[0] = 1
        for i in range(1, len(A)):
            B[i] = B[i-1] * A[i-1]
        tmp = 1
        for i in range(len(A)-2, -1, -1):
            tmp *= A[i+1]
            B[i] *= tmp
        return B


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    print(Solution().multiply1(A))
    # print(dups)
    # print(arr)
