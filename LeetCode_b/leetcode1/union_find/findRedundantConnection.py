# -*- coding: utf-8 -*-
"""
@Time    : 2019/10/4 11:36 AM
@Author  : ddlee
@File    : findRedundantConnection.py
"""
"""

684. 冗余连接
在本问题中, 树指的是一个连通且无环的无向图。

输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。
附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。

结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。

返回一条可以删去的边，使得结果图是一个有着N个节点的树。
如果有多个答案，则返回二维数组中最后出现的边。
答案边 [u, v] 应满足相同的格式 u < v。

示例 1：

输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的无向图为:
  1
 / \
2 - 3
示例 2：

输入: [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]
解释: 给定的无向图为:
5 - 1 - 2
    |   |
    4 - 3
注意:

输入的二维数组大小在 3 到 1000。
二维数组中的整数在1到N之间，其中N是输入数组的大小。
更新(2017-09-26):
我们已经重新检查了问题描述及测试用例，明确图是无向 图。对于有向图详见冗余连接II。对于造成任何不便，我们深感歉意。
"""


class Solution:

    def findRedundantConnection1(self, edges):
        p = {i: {i} for i in range(1, len(edges) + 1)}  # 并查集初始化
        for x, y in edges:
            if p[x] is not p[y]:  # 如果两个集合地址不一样
                p[x] |= p[y]  # 合并集合
                for z in p[y]:
                    p[z] = p[x]  # 修改元素集合标记的指针地址
            else:
                return [x, y]

    def findRedundantConnection(self, edges):
        class UnionFind():
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.redundant = []

            def find(self, p):
                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return self.parent[p]

            def is_connected(self, p, q):
                p_root = self.find(p)
                q_root = self.find(q)
                return p_root == q_root

            def union(self, p, q):
                p_root = self.find(p)
                q_root = self.find(q)
                if p_root != q_root:
                    self.parent[q_root] = p_root
                else:
                    self.redundant.append([p, q])

        l = len(edges)
        uf = UnionFind(l + 1)

        for x, y in edges:
            uf.union(x, y)

        return uf.redundant[-1] if len(uf.redundant) > 0 else None


if __name__ == '__main__':
    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    print(Solution().findRedundantConnection1(edges))
