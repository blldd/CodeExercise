# -*- coding: utf-8 -*-
"""
@Time    : 2019/10/2 4:11 PM
@Author  : ddlee
@File    : findCircleNum.py
"""

"""
547. 朋友圈

班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。
如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。
所谓的朋友圈，是指所有朋友的集合。

给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。
如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。
你必须输出所有学生中的已知的朋友圈总数。

示例 1:
输入: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
 
输出: 2 

说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回2。
"""


class Solution():
    def findCircleNum(self, M):
        class UnionFind():
            def __init__(self, n):
                self.cnt = n
                self.parent = [i for i in range(n)]
                # self.rank = [1 for _ in range(n)]

            def get_cnt(self):
                return self.cnt

            def find(self, p):
                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p

            def is_connected(self, p, q):
                return self.find(p) == self.find(q)

            def union(self, p, q):
                p_root = self.find(p)
                q_root = self.find(q)
                if p_root == q_root:
                    return

                if p_root != q_root:
                    self.parent[q_root] = p_root
                #
                # if self.rank[p_root] > self.rank[q_root]:
                #     self.parent[q_root] = p_root
                # elif self.rank[p_root] < self.rank[q_root]:
                #     self.parent[p_root] = q_root
                # else:
                #     self.parent[q_root] = p_root
                #     self.rank[p_root] += 1
                self.cnt -= 1

        row = len(M)
        # 特判
        if row == 0:
            return 0
        col = len(M[0])

        uf = UnionFind(row)

        for i in range(row):
            for j in range(i + 1, col):
                if M[i][j] == 1:
                    uf.union(i, j)

        return uf.get_cnt()


if __name__ == '__main__':
    # grid = [[1, 0, 0],
    #         [0, 1, 0],
    #         [0, 0, 1]]

    grid = [[1, 0, 0, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 1],
            [1, 0, 1, 1]]
    grid = [[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]]

    print(Solution().findCircleNum(grid))
