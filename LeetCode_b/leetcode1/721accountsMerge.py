# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/19 10:58 PM
@Author  : ddlee
@File    : 721accountsMerge.py
"""
import collections


class Solution:
    def accountsMerge(self, accounts):
        l = len(accounts)
        if l <= 1:
            return accounts

        mail_no_dictt = collections.defaultdict(set)
        for i in range(l):
            for mail in accounts[i][1:]:
                mail_no_dictt[mail].add(i)

        mail_no_dictt = sorted(mail_no_dictt.items(), key=lambda x: len(x[1]), reverse=True)
        print(mail_no_dictt)

        ans = []

        res_dictt = collections.defaultdict(set)

        for i in range(len(mail_no_dictt)):
            for j in range(i + 1, len(mail_no_dictt)):
                un = list(mail_no_dictt[i][1].intersection(mail_no_dictt[j][1]))

                if un:
                    res_dictt[accounts[un[0]][0]].add(mail_no_dictt[i][0])
                    res_dictt[accounts[un[0]][0]].add(mail_no_dictt[j][0])
                else:
                    res_dictt[accounts[list(mail_no_dictt[i][1])[0]][0]].add(mail_no_dictt[i][0])
                    res_dictt[accounts[list(mail_no_dictt[j][1])[0]][0]].add(mail_no_dictt[j][0])

        print(res_dictt)
        return ans

    def accountsMerge_uf(self, accounts):
        d = collections.defaultdict(set)
        c = set()
        n = len(accounts)
        for i in range(n):
            for j in accounts[i][1:]:  # 统计邮箱出现在哪些账户
                for k in d[j]:
                    if i != k:
                        c |= {(k, i)}  # 把判断两个账户是否能够相连哈希化
                d[j] |= {i}
        p = [*range(n)]  # 并查集初始化

        def f(x):  # 并查集修改函数
            if p[x] != x:
                p[x] = f(p[x])
            return p[x]

        for i in range(n):
            for j in range(i + 1, n):
                if (i, j) in c:
                    pi, pj = f(i), f(j)
                    if pi != pj:  # 符合条件的合并集合编号
                        p[pj] = pi
        ans = {}
        for i in range(n):  # 按集合编号合并元素
            pi = f(i)
            if pi not in ans:
                ans[pi] = accounts[i]
            else:
                ans[pi] += accounts[i][1:]
        return [[s[0]] + sorted(list(set(s[1:]))) for s in ans.values()]  # 邮箱列表去重并排序输出


if __name__ == '__main__':
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
                ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["Mary", "mary@mail.com"]]

    print(Solution().accountsMerge_uf(accounts))
