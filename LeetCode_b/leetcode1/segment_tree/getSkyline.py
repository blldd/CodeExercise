# -*- coding: utf-8 -*-
"""
@Time    : 2019/10/4 8:22 PM
@Author  : ddlee
@File    : getSkyline.py
"""

"""
218. 天际线问题

城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。
现在，假设您获得了城市风光照片（图A）上显示的所有建筑物的位置和高度，请编写一个程序以输出由这些建筑物形成的天际线（图B）。
"""

"""
求这些建筑物的所构成的轮廓线，可以理解为要返回轮廓线上每条水平线左边的坐标集合；
离散化 + 线段树
"""


class Node:
    def __init__(self):
        self.l = 0
        self.r = 0
        self.h = 0


class Solution:
    def getSkyline(self, buildings):
        """
                :type buildings: List[List[int]]
                :rtype: List[List[int]]
                """
        global mp, mp2, index, Tree

        mp = {}
        mp2 = {}
        index = []

        if len(buildings) == 0:
            return []

        for i in range(len(buildings)):
            for j in range(2):
                if buildings[i][j] not in mp:
                    mp[buildings[i][j]] = 1
                    index.append(buildings[i][j])
        index.sort()
        for i in range(len(index)):
            mp[index[i]] = i
            mp2[i] = index[i]
        print(index)
        print(mp)
        print(mp2)
        maxn = len(index)
        Tree = [Node() for i in range(maxn << 2)]
        print(Tree)
        self.build(0, maxn, 0)
        res = []
        for i in range(len(buildings)):
            self.update(mp[buildings[i][0]], mp[buildings[i][1]] - 1, buildings[i][2], 0)

        self.query(res, 0)
        return res

    def build(self, l, r, rt):
        Tree[rt].l = l
        Tree[rt].r = r
        if l == r:
            return

        m = (l + r) >> 1
        self.build(l, m, 2 * rt + 1)
        self.build(m + 1, r, 2 * rt + 2)

    def update(self, l, r, h, rt):
        if Tree[rt].h >= h:
            return

        if Tree[rt].l == l and Tree[rt].r == r:
            Tree[rt].h = h
            return

        if Tree[rt].h > 0:
            Tree[2 * rt + 1].h = max(Tree[rt].h, Tree[2 * rt + 1].h)
            Tree[2 * rt + 2].h = max(Tree[rt].h, Tree[2 * rt + 2].h)
            Tree[rt].h = 0

        m = (Tree[rt].l + Tree[rt].r) >> 1
        if r <= m:
            self.update(l, r, h, 2 * rt + 1)
        elif l > m:
            self.update(l, r, h, 2 * rt + 2)
        else:
            self.update(l, m, h, 2 * rt + 2)
            self.update(m + 1, r, h, 2 * rt + 2)

    def query(self, res, rt):
        if Tree[rt].l == Tree[rt].r:
            if res and Tree[rt].h == res[-1][1]:
                return

            tmp = [mp2[Tree[rt].l], Tree[rt].h]
            res.append(tmp)
            return

        if Tree[rt].h > 0:
            Tree[rt * 2 + 1].h = max(Tree[rt].h, Tree[rt * 2 + 1].h)
            Tree[rt * 2 + 2].h = max(Tree[rt].h, Tree[rt * 2 + 2].h)
            Tree[rt].h = 0
        self.query(res, rt * 2 + 1)
        self.query(res, rt * 2 + 2)


if __name__ == '__main__':
    buildings = [[2, 9, 10],
                 [3, 7, 15],
                 [5, 12, 12],
                 [15, 20, 10],
                 [19, 24, 8]]
    print(Solution().getSkyline(buildings))
