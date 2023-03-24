# -*- coding: utf-8 -*-
"""
@Time    : 2019/10/3 10:31 PM
@Author  : ddlee
@File    : accountsMerge.py
"""
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts):

        class UnionFind:
            def __init__(self, n):
                self.cnt = n
                self.parent = [i for i in range(n)]

            def find(self, p):
                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p

            def is_connected(self, p, q):
                p_root = self.find(p)
                q_root = self.find(q)
                return p_root == q_root

            def union(self, p, q):
                p_root = self.find(p)
                q_root = self.find(q)
                if p_root != q_root:
                    self.parent[q_root] = p_root


        lookup = {}
        n = len(accounts)
        uf = UnionFind(n)
        # 第一步，找到相关联的账户，并使用并查集记录
        for idx, account in enumerate(accounts):
            email = account[1:]
            for em in email:
                if em in lookup:
                    uf.union(idx, lookup[em])
                else:
                    lookup[em] = idx

        # 第二步，将相关联账户的邮箱地址合并起来
        joint_account = defaultdict(set)
        for i in range(n):
            root = uf.find(i)
            for em in accounts[i][1:]:
                joint_account[root].add(em)

        # 第三步，输出结果
        res = []
        for key, val in joint_account.items():
            res.append([accounts[key][0]] + list(sorted(val)))

        return res


if __name__ == '__main__':
    accounts = [
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["John", "johnnybravo@mail.com"],
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["Mary", "mary@mail.com"]
    ]

    print(Solution().accountsMerge(accounts))
