# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/8 9:28 AM
@Author  : ddlee
@File    : 547findCircleNum.py
"""


class Solution(object):
    """
    班上有 N 名学生。其中有些人是朋友，有些则不是。
    他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。
    所谓的朋友圈，是指所有朋友的集合。
    给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。
    如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

    示例 1:
    输入:
    [[1,1,0],
     [1,1,0],
     [0,0,1]]
    输出: 2
    说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
    第2个学生自己在一个朋友圈。所以返回2。
    """

    # 超时
    def findCircleNum1(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        res = 0
        friends = []
        for i in range(len(M)):
            for j in range(i, len(M[0])):
                if M[i][j] == 1:
                    friends.append([i, j])
        print(friends)

        length = len(friends)
        if length < 1:
            return res

        for i in range(length):
            for j in range(length):
                if set(friends[i]).intersection(set(friends[j])):
                    friends[i] = friends[j] = list(set(friends[i]).union(set(friends[j])))
        friends = [tuple(sorted(t)) for t in friends]
        print(friends)
        res = len(set(friends))
        return res

    """
    （1）可以先找到一个人，把这个人的所有朋友都入队。 
    （2）然后依次出队，把朋友的朋友都入队，已经入过队列的，则不再入队（是不是广度优先搜索）。 
    （3）直到不再有朋友入队，而且已经出队完成，说明现在已经组成了一个朋友圈。 
    （4）然后把剩下的没被分到朋友圈里面的，同学，再次入队，进行下一个朋友圈的计算，依次循环直到结束。
    """

    def findCircleNum(self, M):
        queue, cnt = [0], 0  # [0] 表示第一个人，题目已经给出至少一个人。 cnt 记录朋友圈的个数
        visited = [0] * len(M)  # 0 表示没有访问过，1 表示已经访问过了。
        visited[0] = 1

        while len(queue):  # 队列不为空
            i = queue.pop()  # 出队一个人
            for j in range(len(M[i])):
                if visited[j] or i == j or M[i][j] == 0:  # 访问过了，或者是自己，或者不是朋友关系，则不加
                    continue
                queue.append(j)  # 入队
                visited[j] = 1  # 此人已经访问过

            if not len(queue):  # 队列为空
                cnt += 1  # 朋友圈数 加一
                if sum(visited) < len(visited):  # 如何还有人没有被分到朋友圈
                    idx = visited.index(0)  # 继续入队一个人
                    queue.append(idx)
                    visited[idx] = 1
        return cnt


class Solu:
    def findCircleNum(self, M) -> int:

        class UnionFind:

            def __init__(self, n):
                self.count = n
                self.parent = [i for i in range(n)]
                self.rank = [1 for _ in range(n)]

            def get_count(self):
                return self.count

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

                if self.rank[p_root] > self.rank[q_root]:
                    self.parent[q_root] = p_root
                elif self.rank[p_root] < self.rank[q_root]:
                    self.parent[p_root] = q_root
                else:
                    self.parent[q_root] = p_root
                    self.rank[p_root] += 1

                self.count -= 1

        m = len(M)
        union_find_set = UnionFind(m)
        for i in range(m):
            for j in range(i):
                if M[i][j] == 1:
                    union_find_set.union(j, i)

        return union_find_set.get_count()


if __name__ == '__main__':
    # grid = [[1, 0, 0],
    #         [0, 1, 0],
    #         [0, 0, 1]]

    grid = [[1, 0, 0, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 1],
            [1, 0, 1, 1]]
    print(Solution().findCircleNum(grid))
    print(Solu().findCircleNum(grid))
