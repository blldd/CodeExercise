# -*- coding:UTF-8 -*-
"""

class Solution:
    def __init__(self):
        self.onePath = []
        self.PathArray = []

    def FindPath(self, root, expectNumber):
        if root is None:
            return self.PathArray
        self.onePath.append(root.val)
        expectNumber -= root.val
        if expectNumber == 0 and not root.left and not root.right:
            self.PathArray.append(self.onePath[:])
        elif expectNumber > 0:
            self.FindPath(root.left, expectNumber)
            self.FindPath(root.right, expectNumber)
        self.onePath.pop()
        return self.PathArray
"""

import sys


class Solution:
    """
    O(N^3)
    """

    def floyed(self, vertex, dis):
        for i in range(len(vertex)):
            for j in range(len(dis)):
                for k in range(len(dis[j])):
                    if dis[i][j] > dis[i][k] + dis[k][j]:
                        dis[i][j] = dis[i][k] + dis[k][j]
        return dis

    """
    典型的二进制堆优先级队列实现具有O（（| E | + | V |）log | V |）
    [Fibonacci堆优先级队列给出O（ | V | log | V | + | E |）]
    不能解决带负权的图
    """

    def dijkstra(self, nodes, distances, current):
        candidates = distances[current]

        # init U set
        unvisited = {}
        for node in nodes:
            if node in candidates:
                unvisited[node] = candidates[node]
            else:
                unvisited[node] = sys.maxsize

        # S set
        visited = unvisited.copy()
        visited[current] = 0
        del unvisited[current]

        while unvisited:
            sort_candidates = sorted(candidates.items(), key=lambda x: x[1])
            current, current_dist = sort_candidates[0]
            visited[current] = current_dist
            del unvisited[current]

            for (neighbour, distance) in distances[current].items():
                new_dist = current_dist + distance
                if visited[neighbour] > new_dist:
                    visited[neighbour] = new_dist

            candidates = {node: visited[node] for node in unvisited}
        return visited

    """
    为什么Dijkstra不可以解决带负权的图？
    其跟本的原因在于，在Dijkstra，一旦一个顶点用来松弛过以后，其最小值已经固定不会再参与到下一次的松弛中。
    因为Dijkstra中全部的距离都是正权，所以不可能出现A - B - C 之间的距离比 A - B - D - C 的距离短的情况，
    而Bellman-Ford则在每次循环中，则会将每个点都重新松弛一遍，所以可以处理负权。

    Bellman-Ford算法具有O（| V || E |）复杂度
    """

    def getEdges(self, G):
        """ 读入图G，返回其边与端点的列表 """

        v1 = []  # 出发点
        v2 = []  # 对应的相邻到达点
        e = []  # 顶点v1到顶点v2的边的权值
        for i in G:
            for j in G[i]:
                if G[i][j] != 0:
                    e.append(G[i][j])
                    v1.append(i)
                    v2.append(j)
        return v1, v2, e

    def Bellman_Ford(self, G, v0, INF=999):
        v1, v2, e = self.getEdges(G)

        # 初始化源点与所有点之间的最短距离
        dis = dict((k, INF) for k in G.keys())
        dis[v0] = 0

        # 核心算法
        for k in range(len(G) - 1):  # 循环 n-1轮
            check = 0  # 用于标记本轮松弛中dis是否发生更新
            for i in range(len(e)):  # 对每条边进行一次松弛操作
                if dis[v1[i]] + e[i] < dis[v2[i]]:
                    dis[v2[i]] = dis[v1[i]] + e[i]
                    check = 1
            if check == 0:
                break

        # 检测负权回路
        # 如果在 n-1 次松弛之后，最短路径依然发生变化，则该图必然存在负权回路
        flag = 0
        for i in range(len(e)):  # 对每条边再尝试进行一次松弛操作
            if dis[v1[i]] + e[i] < dis[v2[i]]:
                flag = 1
                break
        if flag == 1:
            return False
        return dis


if __name__ == "__main__":
    vertex = ["A", "B", "C", "D", "E", "F"]
    dist = [
        [999, 2, 999, 999, 2, 10],
        [999, 999, 999, 999, 999, 6],
        [999, 999, 999, 999, 999, 1],
        [999, 999, 999, 999, 999, 999],
        [999, 999, 1, 999, 999, 999],
        [999, 999, 999, 999, 999, 999],
    ]
    print(Solution().floyed(vertex, dist))

    nodes = ("A", "B", "C", "D", "E", "F")
    distances = {
        "A": {"B": 6, "D": 4, "F": 1},
        "B": {"A": 5, "C": 7, "D": 7},
        "C": {"D": 2, "E": 4},
        "D": {"B": 3, "C": 5, "E": 1, "F": 7},
        "E": {"A": 2, "D": 3},
        "F": {"B": 3, "C": 4, "E": 4},
    }

    print(Solution().dijkstra(nodes, distances, "A"))

    G = {
        "s": {"a": 10, "e": 8},
        "a": {"c": 2},
        "b": {"a": 1},
        "c": {"b": -2},
        "d": {"a": -4, "c": -1},
        "e": {"d": 1},
    }
    v0 = "s"

    distance = Solution().Bellman_Ford(G, v0)  # 查找从源点0开始带其他节点的最短路径
    print(distance)
