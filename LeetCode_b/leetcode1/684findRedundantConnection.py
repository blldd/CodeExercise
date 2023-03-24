# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/22 8:19 AM
@Author  : ddlee
@File    : 684findRedundantConnection.py
"""
import collections

"""
684. 冗余连接
在本问题中, 树指的是一个连通且无环的无向图。
输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。
附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。
返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。

示例 1：
输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的无向图为:
  1
 / \
2 - 3
"""


class Solution:
    def findRedundantConnection1(self, edges):
        # pa_ch_dictt = collections.defaultdict(set)
        ch_pa_dictt = {}

        for edge in edges:
            # pa_ch_dictt[edge[0]].add(edge[1])
            if edge[1] not in ch_pa_dictt:
                tmp_pa = edge[0]
                while tmp_pa in ch_pa_dictt:
                    ch_pa_dictt[edge[1]] = ch_pa_dictt[tmp_pa]
                    tmp_pa = ch_pa_dictt[tmp_pa]

                ch_pa_dictt[edge[1]] = tmp_pa
            else:
                old_pa = ch_pa_dictt[edge[1]]
                tmp_pa = edge[0]
                while tmp_pa in ch_pa_dictt:
                    ch_pa_dictt[edge[1]] = ch_pa_dictt[tmp_pa]
                    tmp_pa = ch_pa_dictt[tmp_pa]
                new_pa = tmp_pa
                if new_pa == old_pa:
                    return edge

        # print(ch_pa_dictt)

    def findRedundantConnection(self, edges):
        p = [*range(len(edges) + 1)]  # 并查集元素初始化

        def f(x):
            if p[x] != x:  # 递归修改所属集合
                p[x] = f(p[x])
            return p[x]

        for x, y in edges:  # 遍历边
            px, py = f(x), f(y)
            if px != py:  # 检查集合，如果集合不同就合并
                p[py] = px
            else:
                return [x, y]  # 集合相同就返回答案

if __name__ == '__main__':
    edges = [[1, 2], [1, 3], [2, 3]]
    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    edges = [[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]]
    print(Solution().findRedundantConnection(edges))
