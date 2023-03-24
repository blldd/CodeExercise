# -*- coding: utf-8 -*-
"""
@Time    : 2019/4/23 3:11 PM
@Author  : ddlee
@File    : 207toposort.py
"""
import collections

"""
现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？

示例 1:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。

==> 判断是否为有向无环图
"""


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)

        indegrees = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegrees[course] += 1

        return self.topologicalSort(graph, indegrees) == numCourses

    def topologicalSort(self, graph, indegrees):
        count = 0
        queue = []
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
        l = []
        while queue:
            course = queue.pop()
            l.append(course)
            count += 1
            for i in graph[course]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    queue.append(i)
        print(l)
        return count


if __name__ == '__main__':
    print(Solution().canFinish(2, [[1, 0]]))
