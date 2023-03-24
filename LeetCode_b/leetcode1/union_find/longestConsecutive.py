# -*- coding: utf-8 -*-
"""
@Time    : 2019/10/4 10:35 AM
@Author  : ddlee
@File    : longestConsecutive.py
"""

"""\
128. 最长连续序列
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
"""


class Solution:
    def longestConsecutive3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        res = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                res = max(res, y - x)
        return res

    def longestConsecutive(self, nums):
        class UnionFind():

            def find(self, p):
                if p not in look_up:
                    return p

                # if look_up[p] != p:
                #     look_up[p] = self.find(look_up[p])
                while p != look_up[p]:
                    look_up[p] = look_up[look_up[p]]
                    p = look_up[p]
                return look_up[p]

        look_up = {}
        uf = UnionFind()

        for x in nums:
            x_root = uf.find(x)
            look_up[x] = x_root
            if x - 1 in look_up:
                look_up[uf.find(x - 1)] = x_root
            if x + 1 in look_up:
                look_up[x_root] = uf.find(x + 1)

        res = 0
        for x in nums:
            res = max(res, uf.find(x) - x + 1)

        return res

    def longestConsecutive1(self, nums):
        class UnionFind():
            def __init__(self):
                self.parent = {}

            def find(self, p):
                if p not in self.parent:
                    return p

                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p

            def union(self, p, q):
                p_root = self.find(p)
                q_root = self.find(q)
                if p_root != q_root:
                    self.parent[q_root] = p_root

        uf = UnionFind()

        for x in nums:
            x_root = uf.find(x)
            uf.parent[x] = x_root

            if x - 1 in uf.parent:
                uf.union(x, x - 1)
                # uf.parent[uf.find(x - 1)] = x_root
            if x + 1 in uf.parent:
                uf.union(x + 1, x)
                # uf.parent[x_root] = uf.find(x + 1)

        res = 0
        for x in nums:
            res = max(res, uf.find(x) - x + 1)

        return res



if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    print(Solution().longestConsecutive1(nums))
